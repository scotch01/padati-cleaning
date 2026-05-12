import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.append(str(ROOT_DIR))

import streamlit as st

from src.preprocessing import preprocess_dataframe
from src.classifier import apply_classification
from src.summary import build_summary
from src.exporter import export_excel
from src.loader import load_excel_sheets


st.set_page_config(
    page_title="Processing",
    layout="wide"
)


st.title("Merchant Processing")

st.markdown(
    "Upload dan proses file merchant scraping"
)


uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)


if uploaded_file:

    raw_dfs = load_excel_sheets(uploaded_file)

    sheet_names = list(raw_dfs.keys())

    st.success(
        f"{len(sheet_names)} sheets detected"
    )

    dfs = {}

    progress = st.progress(0)

    for idx, (sheet, df) in enumerate(raw_dfs.items()):

        # PREPROCESS
        df = preprocess_dataframe(df)

        # CLASSIFY
        df = apply_classification(df)

        dfs[sheet] = df

        progress.progress(
            (idx + 1) / len(sheet_names)
        )

    # =========================================================
    # SUMMARY
    # =========================================================

    summary_df = build_summary(dfs)

    st.subheader("Summary")

    st.dataframe(
        summary_df,
        use_container_width=True
    )


    # =========================================================
    # PREVIEW
    # =========================================================

    st.subheader("Preview Data")

    selected_sheet = st.selectbox(
        "Select Sheet",
        list(dfs.keys())
    )

    selected_status = st.selectbox(
        "Filter Status",
        [
            "ALL",
            "KEEP",
            "REVIEW",
            "REJECT"
        ]
    )

    preview_df = dfs[selected_sheet]

    if selected_status != "ALL":

        preview_df = preview_df[
            preview_df["status"] == selected_status
        ]

    st.dataframe(
        preview_df,
        use_container_width=True,
        height=500
    )


    # =========================================================
    # DOWNLOAD
    # =========================================================

    excel_data = export_excel(
        dfs,
        summary_df
    )

    st.download_button(
        label="Download Cleaned Result",
        data=excel_data,
        file_name="cleaned_result.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )