import pandas as pd

class ExcelEngine:
    """Parses Excel component registers and prepares tag matching."""

    def parse_component_register(self, path: str) -> dict:
        workbook = pd.read_excel(path, sheet_name=None)
        sheets = []
        for name, df in workbook.items():
            sheets.append({
                "sheet": name,
                "rows": len(df),
                "columns": list(df.columns),
            })
        return {"sheets": sheets}
