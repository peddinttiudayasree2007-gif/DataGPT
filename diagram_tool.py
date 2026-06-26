import sqlite3

def get_er_diagram():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(sales)")
    columns = cursor.fetchall()

    conn.close()

    diagram = "erDiagram\n    SALES {\n"

    for col in columns:
        col_name = col[1]
        col_type = col[2]
        diagram += f"        {col_type} {col_name}\n"

    diagram += "    }"

    return diagram