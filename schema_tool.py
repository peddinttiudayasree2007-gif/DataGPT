import sqlite3

def get_schema():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(sales)")
    columns = cursor.fetchall()

    conn.close()

    return columns