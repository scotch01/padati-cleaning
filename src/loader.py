import pandas as pd


def load_excel_sheets(uploaded_file):

    xls = pd.ExcelFile(uploaded_file)

    dfs = {
        sheet: pd.read_excel(
            uploaded_file,
            sheet_name=sheet
        )
        for sheet in xls.sheet_names
    }

    return dfs