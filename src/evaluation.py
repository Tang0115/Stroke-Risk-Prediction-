"""
evaluation.py — Shared metrics and plotting helpers.

Usage example:
    from src.evaluation import evaluate_model, plot_confusion_matrix
    metrics = evaluate_model("My Model", fitted_pipeline, X_test, y_test)
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, RocCurveDisplay,
)


def evaluate_model(name: str, model, X_test, y_test) -> dict:
    """Return a metrics dict for the stroke-positive class."""
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_prob)
    report = classification_report(y_test, y_pred, output_dict=True)

    print(f"\n--- {name} ---")
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC: {auc:.4f}")

    return {
        "model":            name,
        "precision_stroke": report["1"]["precision"],
        "recall_stroke":    report["1"]["recall"],
        "f1_stroke":        report["1"]["f1-score"],
        "roc_auc":          auc,
        "accuracy":         report["accuracy"],
    }


def plot_confusion_matrix(model, X_test, y_test, title: str, save_path: str = None):
    cm = confusion_matrix(y_test, model.predict(X_test))
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax,
                xticklabels=["No Stroke", "Stroke"],
                yticklabels=["No Stroke", "Stroke"])
    ax.set_title(title)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_roc_curve(model, X_test, y_test, name: str, save_path: str = None):
    fig, ax = plt.subplots()
    RocCurveDisplay.from_estimator(model, X_test, y_test, ax=ax, name=name)
    ax.set_title(f"ROC Curve — {name}")
    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150)
    plt.show()
