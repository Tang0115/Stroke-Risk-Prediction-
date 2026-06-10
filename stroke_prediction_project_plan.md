# Stroke Risk Prediction — Project Plan

**Team:** Carley Saeger, Matthew Kallberg, Tom (Xinsheng) Tang, Alina Kanayinkal
**Dataset:** [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data) (5,110 records, 11 predictors, binary target)
**Class ends:** July 7 — plan targets final zip shared by **July 5** to leave buffer.

---

## Phase 1: Data Exploration & Cleaning (June 10–16)

**Goal:** A clean, well-understood dataset ready for modeling.

- Load data in Databricks / VS Code; set up a shared repo or notebook folder so everyone works from the same code.
- EDA: distributions of each attribute, class distribution of `stroke` (expect heavy imbalance, ~5% positive), correlations, outliers in `avg_glucose_level` and `bmi`.
- Handle missing BMI (~4%): compare dropping vs. median/model-based imputation.
- Drop `id`; decide what to do with `gender = "Other"` (1 record) and `smoking_status = "Unknown"`.
- Encode categoricals (one-hot or label encoding); scale numeric features where needed.
- **Note:** proposal says "regression" under item 4 — this is **binary classification**; fix before final submission.

**Deliverables:** EDA notebook with charts, cleaned/processed dataset (covers submission items 3, 4, 8).

## Phase 2: Baseline Modeling (June 15–20)

**Goal:** Working baseline models with honest evaluation.

- Train/test split with stratification; fix a random seed for reproducibility.
- Baseline: logistic regression (plain, then with regularization — L1/L2).
- Evaluate with recall, precision, F1, ROC-AUC, confusion matrix — **not accuracy alone**, since predicting "no stroke" for everyone already gives ~95% accuracy.
- Establish the metric the team optimizes for (recall on stroke class is the usual choice in medical screening).

**Deliverables:** Baseline notebook + metrics table.

## Phase 3: Improved Models & Imbalance Handling (June 18–26)

**Goal:** Compare models and address class imbalance — the core of the study.

- Imbalance strategies: class weights, SMOTE/oversampling, undersampling, threshold tuning. Compare at least two.
- Additional models: decision tree / random forest, gradient boosting, SVM or KNN (pick 2–3 beyond logistic).
- Control overfitting: cross-validation, regularization strength tuning, learning curves (ties to "Balance of MSE & Complexity" in proposal).
- Feature importance: which of age, hypertension, heart disease, glucose, BMI, smoking matter most (logistic coefficients, tree importances).
- Each teammate can own one model family to parallelize.

**Deliverables:** Model comparison table, feature-importance charts (covers item 6's research questions).

## Phase 4: Final Analysis & Slides (June 25–July 1)

**Goal:** Results consolidated into the presentation.

- Pick final model(s); write conclusions: what predicts stroke, how well, limitations. Remember the instructor's warning: **do not expect unrealistic accuracy** — honest reporting of an imbalanced problem scores better than inflated claims.
- Build slides: methods used, model comparisons, conclusions, **with page numbers** (item 7).
- Clean up code into runnable scripts/notebooks; write a brief user manual (how to run, dependencies, file list) for item 9.

**Deliverables:** Final slide deck, cleaned code + user manual.

## Phase 5: Package & Submit (July 1–5)

**Goal:** One zip, shared correctly, before July 7.

- Assemble all 9 items into a single zip:
  1. Project title
  2. Data source description + link
  3. Records/attributes with descriptions
  4. General statistics (records, predictors, CATs, categories, missing %, class distribution, classification target)
  5. Tools/methods used
  6. Detailed problem description
  7. Presentation slides (with page numbers)
  8. Processed dataset (or link)
  9. Code + short user manual
- Name it **Team_X.zip** (replace X with team number).
- **One** member shares via **UST OneDrive** with the instructor — do **not** email it.
- Every teammate verifies the shared link opens before July 7.

---

## Suggested Ownership Split

| Area | Owner |
|------|-------|
| EDA + cleaning | 1 person |
| Baseline + logistic/regularization | 1 person |
| Tree/boosting models + imbalance experiments | 1–2 people |
| Slides + user manual + packaging | shared, 1 lead |

## Risks to Watch

- **Class imbalance** is the biggest technical risk — budget extra time in Phase 3.
- **"Unknown" smoking status** is ~30% of records; treat it as its own category rather than dropping.
- **Data leakage:** impute BMI and apply SMOTE *after* the train/test split, fit only on training data.
- **Last-minute packaging:** the OneDrive sharing step has tripped teams up before; do it days early and verify access.
