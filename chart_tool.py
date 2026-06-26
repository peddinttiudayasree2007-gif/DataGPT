import sqlite3
import matplotlib.pyplot as plt

def revenue_by_region():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT Region, SUM(Revenue)
        FROM sales
        GROUP BY Region
    """)

    data = cursor.fetchall()

    conn.close()

    regions = [row[0] for row in data]
    revenue = [row[1] for row in data]

    plt.figure(figsize=(6,4))
    plt.bar(regions, revenue)

    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")

    plt.savefig("revenue_chart.png")

    return "revenue_chart.png"

def revenue_pie_chart():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Region, SUM(Revenue)
        FROM sales
        GROUP BY Region
    """)

    data = cursor.fetchall()
    conn.close()

    regions = [row[0] for row in data]
    revenue = [row[1] for row in data]

    plt.figure()

    plt.pie(revenue, labels=regions, autopct='%1.1f%%')

    plt.title("Revenue Distribution by Region")

    plt.savefig("revenue_pie.png")

    return "revenue_pie.png"
def revenue_line_chart():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Product, Revenue
        FROM sales
    """)

    data = cursor.fetchall()
    conn.close()

    products = [row[0] for row in data]
    revenue = [row[1] for row in data]

    plt.figure()

    plt.plot(products, revenue, marker='o')

    plt.title("Revenue Trend by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")

    plt.savefig("revenue_line.png")

    return "revenue_line.png"
import sqlite3
import matplotlib.pyplot as plt

def pie_chart():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Region, SUM(Revenue)
    FROM sales
    GROUP BY Region
    """)

    data = cursor.fetchall()

    conn.close()

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct="%1.1f%%")

    plt.title("Revenue Distribution")

    plt.savefig("pie_chart.png")

    plt.close()

    return "pie_chart.png"

def line_chart():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Product, Revenue
    FROM sales
    """)

    data = cursor.fetchall()

    conn.close()

    products = [row[0] for row in data]
    revenue = [row[1] for row in data]

    plt.figure(figsize=(8,5))

    plt.plot(products, revenue, marker="o")

    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")

    plt.savefig("line_chart.png")

    plt.close()

    return "line_chart.png"
