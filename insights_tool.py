def get_insights(results):
    if not results:
        return ["No data found."]

    insights = []
    insights.append(f"Total rows returned: {len(results)}")

    if len(results) > 0:
        insights.append("Query executed successfully.")
        insights.append("Data retrieved from SQLite database.")

    return insights