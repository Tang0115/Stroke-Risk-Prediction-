"""
models.py — Model training wrappers.

Usage example (from a notebook):
    from src.models import get_models, fit_model
    for name, clf in get_models().items():
        fitted = fit_model(clf, X_train, y_train)

All models use class_weight / scale_pos_weight where supported, because the
stroke class is ~5% positive. Tune further in Phase 3.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 42


def get_models() -> dict:
    """Return a dict of {name: untrained estimator} for baseline comparison.

    Add XGBoost / LightGBM / SVM in Phase 3 as needed.
    """
    return {
        "logistic": LogisticRegression(
            max_iter=1000, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "decision_tree": DecisionTreeClassifier(
            class_weight="balanced", random_state=RANDOM_STATE
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=300, class_weight="balanced", random_state=RANDOM_STATE
        ),
    }


def fit_model(model, X_train, y_train):
    """Fit and return the estimator (thin wrapper for a consistent API)."""
    model.fit(X_train, y_train)
    return model
