# DataGPT




**Overview**

DataGPT is an AI-powered conversational database assistant that enables users to interact with databases using natural language.



The system automatically converts user questions into SQL queries, executes them against a database, generates visualizations, and provides business insights.



**Features**



\* Natural Language to SQL

\* SQL Query Transparency

\* CSV Upload

\* SQLite Database Integration

\* Query Execution

\* Dashboard Analytics

\* Bar Chart Visualization

\* Line Chart Visualization

\* Pie Chart Visualization

\* Database Schema Viewer

\* ER Diagram Generator

\* Flowchart Generator

\* Query History

\* Data Explanation and Insights



**Technology Stack**

Backend

\* FastAPI

\* Python

\* SQLite



Data Processing

\* Pandas

\* SQLAlchemy



Visualization

\* Matplotlib

\* Mermaid



Frontend

\* HTML

\* CSS

\* JavaScript



APIs

Chat

POST /chat

Upload CSV

POST /upload-csv

Dashboard

GET /dashboard

Schema

GET /schema

Flowchart

GET /flowchart

ER Diagram

GET /er-diagram

History

GET /history



**Run Locally**

Install dependencies:

pip install -r requirements.txt



**Run application:**

uvicorn main:app –reload



Open:

http://127.0.0.1:8000



**Project Structure**



backend/

\* main.py

\* sql\_agent.py

\* chart\_tool.py

\* schema\_tool.py

\* diagram\_tool.py

\* flowchart\_tool.py

\* explain\_tool.py

\* index.html

\* dashboard.html

\* flowchart.html

\* database.db

\* requirements.txt

\* README.md


DataGPT – An intelligent LLM agent that enables natural language interaction with databases, automatic SQL generation, data visualization, and AI-powered insights.

