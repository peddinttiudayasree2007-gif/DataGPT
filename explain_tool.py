def explain_data(results):

    if not results:
        return "No data found."

    return f"""
The query returned {len(results)} records.
The data was successfully retrieved from the database.
This information can be used for business analysis.
"""