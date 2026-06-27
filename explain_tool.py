# explain_tool.py

import pandas as pd

def explain_data(results):
    if not results:
        return "No data found."

    try:
        df = pd.DataFrame(results)

        return (
            f"The query returned {len(df)} rows "
            f"and {len(df.columns)} columns."
        )

    except Exception:
        return "Query executed successfully."