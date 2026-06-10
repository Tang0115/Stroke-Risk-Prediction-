# Stroke Risk Prediction — SEIS 763 Machine Learning Project

**Team:** Carley Saeger · Matthew Kallberg · Tom (Xinsheng) Tang · Alina Kanayinkal  
**Course:** SEIS 763 Machine Learning — University of St. Thomas  
**Dataset:** [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data) (5,110 records, 11 predictors, binary target `stroke`)  
**Final submission deadline:** July 5, 2026 (class ends July 7)

---

## Project Goal

Build and evaluate machine learning classifiers to predict whether a patient is at risk of stroke using demographic and clinical features. The core challenge is **severe class imbalance** (~5% positive class), so the team explicitly targets recall, F1, and ROC-AUC rather than raw accuracy.

---

## Repository Structure

```
stroke-risk-prediction/
├── data/
│   ├── raw/                    # Original Kaggle CSV (do NOT commit large files — see .gitignore)
│   └── processed/              # Cleaned & encoded dataset produced by Phase 1
├── notebooks/
│   ├── phase1_eda/
│   │   └── 01_eda_cleaning.ipynb
│   ├── phase2_baseline/
│   │   └── 02_baseline_logistic.ipynb
│   ├── phase3_advanced_models/
│   │   └── 03_advanced_models.ipynb
│   └── phase4_final_analysis/
│       └── 04_final_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── data.py                 # Kaggle dataset download helper
│   ├── preprocessing.py        # Cleaning & encoding helpers
│   ├── features.py             # Feature engineering utilities
│   ├── models.py               # Model training wrappers
│   └── evaluation.py           # Metrics & plotting helpers
├── results/
│   ├── figures/                # Saved plots (PNG/SVG)
│   └── metrics/                # Saved metrics tables (CSV/JSON)
├── docs/
│   └── user_manual.md          # How to run the project end-to-end
├── .gitignore
├── CONTRIBUTING.md
├── requirements.txt
└── README.md
```

---

## Phases & Timeline

### Phase 1 — Data Exploration & Cleaning `June 10–16`
**Owner:** TBD · **Notebook:** `notebooks/phase1_eda/01_eda_cleaning.ipynb`

- [ ] Load raw CSV; quick sanity checks (shape, dtypes, nulls)
- [ ] EDA: distributions, class imbalance check (`stroke` ≈ 5% positive), correlation heatmap
- [ ] Outlier inspection for `avg_glucose_level` and `bmi`
- [ ] Handle missing BMI (~4%): compare drop vs. median vs. model-based imputation
- [ ] Drop `id`; handle `gender = "Other"` (1 record) and `smoking_status = "Unknown"` (~30% → keep as its own category)
- [ ] Encode categoricals (one-hot); scale numerics as needed
- [ ] Save cleaned dataset to `data/processed/`

**Deliverables:** EDA notebook with charts, `data/processed/stroke_cleaned.csv`  
**Submission items covered:** 3, 4, 8

---

### Phase 2 — Baseline Modeling `June 15–20`
**Owner:** TBD · **Notebook:** `notebooks/phase2_baseline/02_baseline_logistic.ipynb`

- [ ] Stratified train/test split (fix `random_state=42`)
- [ ] Logistic Regression baseline (no tuning)
- [ ] Logistic Regression with L1 and L2 regularization
- [ ] Evaluation: confusion matrix, precision, recall, F1, ROC-AUC  
  > **Do not use accuracy as the primary metric** — predicting "no stroke" for every record already yields ~95% accuracy on this dataset.
- [ ] Agree as a team on the primary optimization metric (recommend: **recall on the stroke class**)
- [ ] Save metrics table to `results/metrics/phase2_baseline_metrics.csv`

**Deliverables:** Baseline notebook, metrics table

---

### Phase 3 — Advanced Models & Imbalance Handling `June 18–26`
**Owner:** 1–2 people · **Notebook:** `notebooks/phase3_advanced_models/03_advanced_models.ipynb`

- [ ] Imbalance strategies: `class_weight='balanced'`, SMOTE, undersampling, threshold tuning — compare ≥2
  > **Important:** Apply SMOTE and BMI imputation *after* the train/test split, fitted only on training data
- [ ] Additional model families (pick 2–3):
  - [ ] Decision Tree / Random Forest
  - [ ] Gradient Boosting (XGBoost or LightGBM)
  - [ ] SVM or KNN
- [ ] Cross-validation (StratifiedKFold) and learning curves to detect overfitting
- [ ] Feature importance: logistic coefficients, tree-based importances
- [ ] Model comparison table across all metrics
- [ ] Save figures to `results/figures/`

**Deliverables:** Model comparison table, feature-importance charts  
**Submission items covered:** 6 (research questions)

---

### Phase 4 — Final Analysis & Slides `June 25–July 1`
**Owner:** Shared (1 lead for slides) · **Notebook:** `notebooks/phase4_final_analysis/04_final_analysis.ipynb`

- [ ] Select the final model(s); document the decision rationale
- [ ] Write conclusions: which features predict stroke, how well, and what the limitations are
  > Instructor note: **honest reporting of an imbalanced problem scores better than inflated claims**
- [ ] Build slide deck: methods, model comparisons, conclusions — **include page numbers** (submission item 7)
- [ ] Clean up all notebooks so they run top-to-bottom with no errors
- [ ] Write `docs/user_manual.md` (how to run, dependencies, file list)

**Deliverables:** Final slide deck, polished notebooks, user manual  
**Submission items covered:** 5, 7, 9

---

### Phase 5 — Package & Submit `July 1–5`
**Owner:** 1 lead (verify with whole team)

- [ ] Assemble all 9 required submission items (see checklist below)
- [ ] Name the zip **Team_X.zip** (replace X with your team number)
- [ ] One member shares via **UST OneDrive** — do NOT email
- [ ] **Every teammate verifies the shared link opens** before July 7

#### Submission Checklist
| # | Item | Status |
|---|------|--------|
| 1 | Project title | ☐ |
| 2 | Data source description + link | ☐ |
| 3 | Records/attributes with descriptions | ☐ |
| 4 | General statistics (records, predictors, CATs, missing %, class distribution) | ☐ |
| 5 | Tools/methods used | ☐ |
| 6 | Detailed problem description | ☐ |
| 7 | Presentation slides (with page numbers) | ☐ |
| 8 | Processed dataset (or link) | ☐ |
| 9 | Code + short user manual | ☐ |

---

## Ownership Split

| Area | Owner |
|------|-------|
| EDA + data cleaning (Phase 1) | TBD |
| Baseline models + logistic regression (Phase 2) | TBD |
| Tree/boosting models + imbalance experiments (Phase 3) | TBD |
| Slides + user manual + packaging (Phase 4–5 lead) | TBD |

> Update this table in your first team sync.

---

## Key Risks

| Risk | Mitigation |
|------|-----------|
| Class imbalance (~5% positive) | Budget extra time in Phase 3; always evaluate recall |
| "Unknown" smoking status (~30%) | Keep as its own category — do **not** drop |
| Data leakage | Impute BMI and apply SMOTE *after* split, fit only on train |
| Last-minute packaging | Complete OneDrive sharing by July 1 and verify access |

---

## Quick Setup

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd stroke-risk-prediction

# 2. Create and activate a virtual environment (Python 3.10+)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add the Kaggle dataset (two options)
#    a) Manual: download from
#       https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data
#       and place healthcare-dataset-stroke-data.csv in data/raw/
#    b) API: set up Kaggle credentials once (see docs/user_manual.md), then the
#       Phase 1 notebook auto-downloads it via src/data.py — no manual step.

# 5. Run notebooks in order
#    notebooks/phase1_eda → phase2_baseline → phase3_advanced_models → phase4_final_analysis
```

See `docs/user_manual.md` for the complete run guide.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for branch naming, commit conventions, and pull request workflow.
