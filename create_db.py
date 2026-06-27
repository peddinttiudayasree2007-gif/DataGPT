import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    Product TEXT,
    Region TEXT,
    Revenue INTEGER,
    Quantity INTEGER
)
""")

cursor.execute("DELETE FROM sales")

cursor.executemany(
    "INSERT INTO sales VALUES (?,?,?,?)",
    [
        ("Laptop","North",50000,5),
        ("Mobile","South",30000,8),
        ("Tablet","East",20000,6),
        ("Laptop","West",45000,4),
        ("Mobile","North",25000,7)
    ]
)

conn.commit()
conn.close()

print("Database created successfully.")