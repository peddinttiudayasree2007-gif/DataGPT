import sqlite3

DB_NAME = "database.db"

def query_database(question):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    question = question.lower()

    # Total Revenue
    if "total revenue" in question:

        sql = "SELECT SUM(Revenue) FROM sales"

        cursor.execute(sql)
        total = cursor.fetchone()[0]

        answer = f"Total Revenue = {total}"

        results = [(total,)]

    # Revenue by Region
    elif "revenue" in question and "region" in question:

        sql = """
        SELECT Region, SUM(Revenue)
        FROM sales
        GROUP BY Region
        """

        cursor.execute(sql)
        results = cursor.fetchall()

        answer = ""

        for region, revenue in results:
            answer += f"{region} : {revenue}\n"

    # Show all data
    elif "show" in question or "all" in question:

        sql = "SELECT * FROM sales"

        cursor.execute(sql)

        results = cursor.fetchall()

        answer = ""

        for row in results:
            answer += str(row) + "\n"

    else:

        sql = "SELECT * FROM sales LIMIT 5"

        cursor.execute(sql)

        results = cursor.fetchall()

        answer = ""

        for row in results:
            answer += str(row) + "\n"

    conn.close()

    return {
        "sql": sql,
        "answer": answer,
        "results": results
    }