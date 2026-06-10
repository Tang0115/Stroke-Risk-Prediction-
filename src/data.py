"""
data.py — Dataset download helper (Kaggle API).

Lets teammates pull the raw CSV programmatically instead of downloading by hand.
Needs Kaggle credentials once per machine (see docs/user_manual.md):
    - Create a Kaggle account → Account → "Create New API Token"
    - Save kaggle.json to  ~/.kaggle/kaggle.json   (Windows: C:\\Users\\<you>\\.kaggle\\)

Usage (from a notebook):
    from src.data import ensure_dataset
    RAW_PATH = ensure_dataset()      # downloads only if missing, returns path
    df = pd.read_csv(RAW_PATH)
"""

import os
import shutil

KAGGLE_SLUG = "fedesoriano/stroke-prediction-dataset"
CSV_NAME = "healthcare-dataset-stroke-data.csv"
DEFAULT_RAW_DIR = os.path.join("..", "..", "data", "raw")


def ensure_dataset(raw_dir: str = DEFAULT_RAW_DIR) -> str:
    """Return path to the raw CSV, downloading from Kaggle if not present.

    Tries kagglehub first (simplest), falls back to the kaggle CLI package.
    """
    target = os.path.join(raw_dir, CSV_NAME)
    if os.path.exists(target):
        return target

    os.makedirs(raw_dir, exist_ok=True)

    # Preferred: kagglehub (pip install kagglehub)
    try:
        import kagglehub
        cache_dir = kagglehub.dataset_download(KAGGLE_SLUG)
        src = os.path.join(cache_dir, CSV_NAME)
        shutil.copy(src, target)
        return target
    except ImportError:
        pass

    # Fallback: official kaggle package (pip install kaggle)
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(KAGGLE_SLUG, path=raw_dir, unzip=True)
    return target
