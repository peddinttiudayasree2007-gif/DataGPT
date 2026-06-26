import sqlite3

def query_database(user_question):

    question = user_question.lower()

    # Rule-based SQL generation
    if "total revenue" in question:
        sql_query = "SELECT SUM(Revenue) AS TotalRevenue FROM sales"

    elif "revenue by region" in question:
        sql_query = """
        SELECT Region, SUM(Revenue) AS Revenue
        FROM sales
        GROUP BY Region
        """

    elif "all data" in question:
        sql_query = "SELECT * FROM sales"

    elif "products" in question:
        sql_query = "SELECT Product FROM sales"

    elif "chart" in question:
        sql_query = """
        SELECT Region, SUM(Revenue)
        FROM sales
        GROUP BY Region
        """

    else:
        sql_query = "SELECT * FROM sales LIMIT 10"

    print("SQL QUERY:")
    print(sql_query)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(sql_query)
    results = cursor.fetchall()

    conn.close()

    # Generate answer
    if "total revenue" in question:
        answer = f"Total Revenue = {results[0][0]}"

    elif "revenue by region" in question:
        answer = "\n".join(
            [f"{row[0]} : {row[1]}" for row in results]
        )

    else:
        answer = f"Found {len(results)} record(s)."

    return {
        "sql": sql_query,
        "results": results,
        "answer": answer
    }