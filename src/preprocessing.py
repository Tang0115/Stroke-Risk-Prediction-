"""
preprocessing.py — Data cleaning and encoding helpers.

Usage example (from a notebook):
    from src.preprocessing import load_and_clean, encode_features
    df_clean = load_and_clean("../../data/raw/healthcare-dataset-stroke-data.csv")
    df_encoded = encode_features(df_clean)
"""

import pandas as pd
import numpy as np


def load_and_clean(raw_path: str) -> pd.DataFrame:
    """Load raw CSV and apply cleaning steps."""
    df = pd.read_csv(raw_path)

    # Drop non-predictive ID column
    df.drop(columns=["id"], inplace=True)

    # Remove the single 'Other' gender record
    df = df[df["gender"] != "Other"].copy()

    # Impute missing BMI with training-set median
    # NOTE: when using a train/test split, compute the median on train only
    bmi_median = df["bmi"].median()
    df["bmi"] = df["bmi"].fillna(bmi_median)

    # 'Unknown' smoking_status is kept as its own category (~30% of records)

    return df.reset_index(drop=True)


def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    """One-hot encode categorical columns."""
    cat_cols = [
        "gender", "ever_married", "work_type",
        "Residence_type", "smoking_status"
    ]
    df_enc = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    return df_enc
