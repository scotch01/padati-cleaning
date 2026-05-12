import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))

import streamlit as st


st.set_page_config(
    page_title="Merchant Cleaning Engine",
    layout="wide"
)


st.title("Merchant Cleaning Engine")

st.markdown(
    """
    Sistem cleaning dan klasifikasi merchant hasil scraping
    e-commerce berbasis rule-based geographic filtering.
    """
)


# =========================================================
# OVERVIEW
# =========================================================

st.header("Overview")

st.markdown(
    """
    Aplikasi ini dibuat untuk membantu proses filtering dan
    pembersihan data merchant hasil scraping dari berbagai
    platform e-commerce seperti:

    - GoFood
    - Shopee
    - Tokopedia
    - Blibli

    Fokus utama sistem:

    ```text
    Mengidentifikasi merchant yang kemungkinan berada
    di wilayah Kota Pariaman.
    ```
    """
)


# =========================================================
# WORKFLOW
# =========================================================

st.header("Workflow")

st.markdown(
    """
    ### 1. Upload Excel

    User mengupload file Excel multi-sheet hasil scraping.

    ---

    ### 2. Automatic Cleaning

    Sistem melakukan:

    - standardisasi kolom
    - normalisasi text
    - keyword extraction
    - geographic classification

    ---

    ### 3. Classification

    Setiap merchant diklasifikasikan menjadi:

    | Status | Arti |
    |---|---|
    | KEEP | strong signal Kota Pariaman |
    | REVIEW | ambigu / perlu review manual |
    | REJECT | strong signal luar wilayah |

    ---

    ### 4. Export Result

    Hasil cleaning dapat didownload dalam format Excel.
    """
)


# =========================================================
# STATUS EXPLANATION
# =========================================================

st.header("Status Explanation")


st.subheader("KEEP")

st.markdown(
    """
    Merchant memiliki strong signal wilayah Kota Pariaman.

    Contoh:

    ```text
    Kota Pariaman
    ```

    Data dengan status KEEP dianggap paling relevan.
    """
)


st.subheader("REVIEW")

st.markdown(
    """
    Merchant ambigu atau tidak memiliki signal geografis kuat.

    Contoh:

    ```text
    Toko Jaya
    Kedai Uni
    Pariaman
    ```

    Status REVIEW tidak langsung dianggap valid
    ataupun invalid.

    Biasanya membutuhkan pengecekan manual.
    """
)


st.subheader("REJECT")

st.markdown(
    """
    Merchant memiliki strong signal luar wilayah.

    Contoh:

    ```text
    Jakarta
    Bekasi
    Bukittinggi
    Bandar Buat
    Lubuk Begalung
    ```

    Merchant dengan status REJECT dianggap
    berada di luar target wilayah.
    """
)


# =========================================================
# SUMMARY EXPLANATION
# =========================================================

st.header("Summary Table")

st.markdown(
    """
    Tabel summary menampilkan statistik hasil klasifikasi.

    | Column | Description |
    |---|---|
    | total_rows | total merchant dalam sheet |
    | keep | merchant valid Kota Pariaman |
    | review | merchant ambigu |
    | reject | merchant luar wilayah |

    Summary membantu user memahami kualitas data
    hasil scraping.
    """
)


# =========================================================
# WHY PADANG PARIAMAN IS INCLUDED
# =========================================================

st.header("Why 'Padang Pariaman' Is Included?")

st.markdown(
    """
    Salah satu tantangan terbesar pada project ini adalah:

    ```text
    platform e-commerce tidak memberikan metadata lokasi
    yang konsisten.
    ```

    Banyak merchant menggunakan:

    ```text
    Padang Pariaman
    Kab. Padang Pariaman
    Pariaman
    ```

    sebagai lokasi.

    Padahal:

    ```text
    Kota Pariaman
    dan
    Kabupaten Padang Pariaman
    adalah wilayah administratif berbeda.
    ```

    Namun dalam praktik nyata:

    - merchant sering salah input lokasi
    - platform menggunakan geolocation tidak akurat
    - scraping source sangat noisy

    Karena itu:

    sistem menggunakan:

    ```text
    rule-based contextual filtering
    ```

    untuk mengurangi false positive.
    """
)


# =========================================================
# ENGINE ARCHITECTURE
# =========================================================

st.header("Engine Architecture")

st.markdown(
    """
    Sistem menggunakan pipeline:

    ```text
    Excel Ingestion
    ↓
    Text Normalization
    ↓
    Geographic Signal Detection
    ↓
    Rule-Based Classification
    ↓
    Export Result
    ```

    Engine saat ini menggunakan:

    - keyword matching
    - phrase matching
    - contextual filtering
    - geographic rule engine
    """
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Merchant Cleaning Engine — Rule-Based Geographic Entity Resolution"
)