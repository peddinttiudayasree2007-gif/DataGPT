from insights_tool import get_insights
from history import history
from fastapi.responses import FileResponse
import csv

from explain_tool import explain_data
from flowchart_tool import get_flowchart
from chart_tool import line_chart
from chart_tool import pie_chart
from schema_tool import get_schema
from chart_router import generate_chart
from diagram_tool import get_er_diagram
from chart_tool import revenue_by_region
from sql_agent import query_database
from gemini_helper import ask_gemini

import pandas as pd
import sqlite3

from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    try:
        # 1. SQL agent execution
        result = query_database(request.message)        
        explanation = explain_data(result["results"])
        insights = get_insights(result["results"])
        response = {
            "question": request.message,
            "sql": result["sql"],
            "answer": result["answer"],
            "results": result["results"],
            "explanation": explanation,
            "insights": insights
        }

        if "revenue" in request.message.lower() and "region" in request.message.lower():
            revenue_by_region()   # Generate the chart
            response["chart"] = "revenue_chart.png"
        history.append({
           "question": request.message,
           "sql": result["sql"],
           "answer": result["answer"]
        })
        return response    
    except Exception as e:

        return {
            "error": str(e)
        }
@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):

    # Step 1: Read CSV file
    df = pd.read_csv(file.file)

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Step 2: Connect to SQLite database
    conn = sqlite3.connect("database.db")

    # Step 3: Save CSV into table called "sales"
    df.to_sql(
        "sales",
        conn,
        if_exists="replace",
        index=False
    )

    # Step 4: Close connection
    conn.close()

    # Step 5: Return response
    return {
        "message": "Data stored successfully",
        "rows": len(df),
        "columns": list(df.columns)
    }
@app.get("/data")
def get_data():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()

    conn.close()

    result = [dict(row) for row in rows]

    return {
        "rows": len(result),
        "data": result
    }
@app.get("/chart")
def get_chart():

    chart_path = revenue_by_region()

    return {
        "message": "Chart generated",
        "file": chart_path
    }
@app.get("/er-diagram")
def er_diagram():
    return {
        "diagram": get_er_diagram()
    }
@app.get("/schema")
def schema():

    return {
        "schema": get_schema()
    }

@app.get("/pie-chart")
def get_pie_chart():

    chart_path = pie_chart()

    return {
        "message": "Pie Chart Generated",
        "file": chart_path
    }


@app.get("/line-chart")
def get_line_chart():

    chart_path = line_chart()

    return {
        "message": "Line Chart Generated",
        "file": chart_path
    }


@app.get("/flowchart-ui")
def flowchart_ui():
    return FileResponse("flowchart.html")

@app.get("/flowchart")
def flowchart():

    return {
        "diagram": """
flowchart TD

A[Upload CSV]
B[Store in SQLite]
C[Generate SQL]
D[Execute Query]
E[Generate Chart]
F[Display Result]

A --> B
B --> C
C --> D
D --> E
E --> F
"""
    }


@app.post("/export-csv")
def export_csv(request: ChatRequest):

    result = query_database(request.message)

    filename = "query_results.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        for row in result["results"]:
            writer.writerow(row)

    return FileResponse(
        filename,
        media_type="text/csv",
        filename=filename
    )
@app.get("/history")
def get_history():
    return {
        "history": history
    }
@app.post("/explain")
def explain(request: ChatRequest):

    result = query_database(request.message)

    explanation = explain_data(result["results"])
    insights = get_insights(result["results"])

    return {
        "sql": result["sql"],
        "explanation": explanation,
        "insights": insights
    }

@app.get("/dashboard")
def dashboard():

    conn = sqlite3.connect("database.db")

    total_revenue = pd.read_sql(
        "SELECT SUM(Revenue) AS total FROM sales",
        conn
    )

    regions = pd.read_sql(
        """
        SELECT Region,
        SUM(Revenue) AS Revenue
        FROM sales
        GROUP BY Region
        """,
        conn
    )

    conn.close()

    return {
        "total_revenue": int(total_revenue["total"][0]),
        "regions": regions.to_dict(orient="records")
    }

@app.get("/dashboard-ui")
def dashboard_ui():
    return FileResponse("dashboard.html")


@app.get("/")
def home():
    return FileResponse("index.html")

app.mount("/", StaticFiles(directory=".", html=True), name="static")