from io import BytesIO

import pandas as pd


def export_excel(dfs, summary_df):

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        # SUMMARY
        summary_df.to_excel(
            writer,
            sheet_name="SUMMARY",
            index=False
        )

        # EXPORT PER SHEET
        for sheet, df in dfs.items():

            safe_sheet = sheet[:20]

            # FULL DATA
            df.to_excel(
                writer,
                sheet_name=safe_sheet,
                index=False
            )

            # KEEP
            df[
                df["status"] == "KEEP"
            ].to_excel(
                writer,
                sheet_name=f"{safe_sheet}_KEEP",
                index=False
            )

            # REVIEW
            df[
                df["status"] == "REVIEW"
            ].to_excel(
                writer,
                sheet_name=f"{safe_sheet}_REVIEW",
                index=False
            )

            # REJECT
            df[
                df["status"] == "REJECT"
            ].to_excel(
                writer,
                sheet_name=f"{safe_sheet}_REJECT",
                index=False
            )

    output.seek(0)

    return output