from schema_tool import get_schema

def get_er_diagram():

    schema = get_schema()

    diagram = "erDiagram\n"

    for table, columns in schema.items():

        diagram += f"{table} {{\n"

        for column in columns:

            diagram += f" string {column}\n"

        diagram += "}\n"

    return diagram