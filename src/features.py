"""
features.py — Feature engineering utilities.

Usage example (from a notebook):
    from src.features import scale_numeric, add_age_bins
    df = add_age_bins(df)
    X_train_s, X_test_s, scaler = scale_numeric(X_train, X_test)
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

NUMERIC_COLS = ["age", "avg_glucose_level", "bmi"]


def scale_numeric(X_train: pd.DataFrame, X_test: pd.DataFrame,
                  cols: list = None):
    """Standard-scale numeric columns.

    Fit the scaler on TRAIN ONLY, then transform both sets — avoids leakage.
    Returns (X_train_scaled, X_test_scaled, fitted_scaler).
    """
    cols = cols or [c for c in NUMERIC_COLS if c in X_train.columns]
    scaler = StandardScaler()

    X_train = X_train.copy()
    X_test = X_test.copy()
    X_train[cols] = scaler.fit_transform(X_train[cols])
    X_test[cols] = scaler.transform(X_test[cols])
    return X_train, X_test, scaler


def add_age_bins(df: pd.DataFrame) -> pd.DataFrame:
    """Add a categorical age-group column (optional engineered feature)."""
    df = df.copy()
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 18, 40, 60, 120],
        labels=["child", "young_adult", "middle_age", "senior"],
    )
    return df
