import pandas as pd


def build_summary(dfs):

    summary_rows = []

    for sheet, df in dfs.items():

        counts = (
            df["status"]
            .value_counts()
            .to_dict()
        )

        summary_rows.append({
            "sheet": sheet,
            "total_rows": len(df),
            "keep": counts.get("KEEP", 0),
            "review": counts.get("REVIEW", 0),
            "reject": counts.get("REJECT", 0),
        })

    return pd.DataFrame(summary_rows)