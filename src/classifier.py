import pandas as pd

from src.preprocessing import normalize_text

from src.config import (
    VALID_PHRASES,
    INVALID_PHRASES,
)


def classify_location(text):

    text = normalize_text(text)

    # KEEP
    for phrase in VALID_PHRASES:

        if phrase in text:

            return pd.Series({
                "status": "KEEP",
                "matched_rule": phrase,
                "confidence_score": 100
            })

    # REJECT
    for phrase in INVALID_PHRASES:

        if phrase in text:

            return pd.Series({
                "status": "REJECT",
                "matched_rule": phrase,
                "confidence_score": -100
            })

    # REVIEW
    return pd.Series({
        "status": "REVIEW",
        "matched_rule": "none",
        "confidence_score": 0
    })


def apply_classification(df):

    cols_to_drop = [
        "status",
        "matched_rule",
        "confidence_score"
    ]

    existing_cols = [
        col for col in cols_to_drop
        if col in df.columns
    ]

    if existing_cols:

        df = df.drop(
            columns=existing_cols
        )

    result = df[
        "combined_text"
    ].apply(classify_location)

    df = pd.concat(
        [df, result],
        axis=1
    )

    return df