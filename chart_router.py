from chart_tool import revenue_by_region
from chart_tool import pie_chart
from chart_tool import line_chart

def generate_chart(chart_type):

    if chart_type == "bar":
        return revenue_by_region()

    elif chart_type == "pie":
        return pie_chart()

    elif chart_type == "line":
        return line_chart()

    return None