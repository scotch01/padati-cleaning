import pandas as pd
import re


TEXT_COLUMNS = [
    "merchant_name",
    "address",
    "province_name",
    "regency_name",
    "district_name",
]


RENAME_MAP = {
    "merchantname": "merchant_name",
    "merchanturl": "merchant_url",
    "provincename": "province_name",
    "regencyname": "regency_name",
    "districtname": "district_name",
}


def normalize_text(text):

    if pd.isna(text):
        return ""

    text = str(text).lower()

    text = re.sub(r"[^a-z0-9\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def standardize_columns(df):

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    df.rename(
        columns=RENAME_MAP,
        inplace=True
    )

    return df


def preprocess_dataframe(df):

    df = standardize_columns(df)

    for col in TEXT_COLUMNS:

        if col in df.columns:

            df[col] = (
                df[col]
                .astype(str)
                .apply(normalize_text)
            )

    merchant = df.get("merchant_name", "")
    address = df.get("address", "")

    df["combined_text"] = (
        merchant.fillna("") + " " +
        address.fillna("")
    )

    df["combined_text"] = (
        df["combined_text"]
        .apply(normalize_text)
    )

    return df