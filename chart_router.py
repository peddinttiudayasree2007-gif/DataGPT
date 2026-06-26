from chart_tool import revenue_pie_chart, revenue_line_chart

def generate_chart(user_query: str):

    q = user_query.lower()

    if "region" in q or "distribution" in q:
        return revenue_pie_chart()

    elif "trend" in q or "over time" in q:
        return revenue_line_chart()

    else:
        return None