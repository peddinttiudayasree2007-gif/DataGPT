def get_insights(results):

    if not results:
        return [
            "No data available."
        ]

    revenues = []

    for row in results:

        if len(row) > 1 and isinstance(row[1], (int, float)):
            revenues.append(row[1])

    if not revenues:
        return [
            "Data retrieved successfully."
        ]

    highest = max(revenues)
    lowest = min(revenues)

    return [
        f"Highest value: {highest}",
        f"Lowest value: {lowest}",
        f"Total records: {len(results)}"
    ]