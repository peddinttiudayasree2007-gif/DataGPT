def get_flowchart():

    return """
flowchart TD

A[Upload CSV]
B[Store in SQLite]
C[Generate SQL]
D[Execute Query]
E[Generate Chart]
F[Display Results]

A --> B
B --> C
C --> D
D --> E
E --> F
"""