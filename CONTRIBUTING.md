# Contributing Guide

This document covers how teammates collaborate on the project — branching, commits, pull requests, and notebook conventions.

---

## Branch Strategy

```
main            ← stable, always runnable
│
├── phase1/eda-cleaning        ← Phase 1 work
├── phase2/baseline-models     ← Phase 2 work
├── phase3/advanced-models     ← Phase 3 work
└── phase4/final-analysis      ← Phase 4 work
```

**Rules:**
- Never commit directly to `main`.
- Create a branch from `main` when starting your phase/task.
- Open a pull request when your notebook runs top-to-bottom without errors.
- Get at least one teammate to review before merging.

---

## Branch Naming Convention

```
phase<N>/<short-description>
```

Examples:
- `phase1/eda-cleaning`
- `phase2/logistic-l2`
- `phase3/smote-random-forest`

---

## Commit Messages

Use short, descriptive messages in the imperative form:

```
add EDA distribution plots
fix BMI imputation data leakage
train random forest with SMOTE
update metrics table with AUC scores
```

---

## Notebook Conventions

1. **Run top-to-bottom, no errors** before pushing. Use `Kernel > Restart & Run All`.
2. **First cell** — purpose comment + author + date last run.
3. **Fix random seed** everywhere: `random_state=42`.
4. **Save outputs** to `results/figures/` and `results/metrics/` — do not rely on inline cell output alone.
5. **No hardcoded absolute paths** — use relative paths from the repo root:
   ```python
   import os
   DATA_RAW = os.path.join("..", "..", "data", "raw")
   ```
6. Clear all cell outputs before committing (keeps diffs readable):
   - VS Code: right-click notebook → *Clear All Outputs*
   - Jupyter: *Cell > All Output > Clear*

---

## Pull Request Checklist

Before opening a PR, confirm:

- [ ] Branch is up to date with `main` (`git pull origin main`)
- [ ] Notebook runs top-to-bottom without errors
- [ ] Cell outputs are cleared
- [ ] New figures saved to `results/figures/`
- [ ] New metrics saved to `results/metrics/`
- [ ] `requirements.txt` updated if you added a new library
- [ ] README phase checklist items marked done (if applicable)

---

## Setting Up Git (first time)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Then clone the repo:

```bash
git clone <repo-url>
cd stroke-risk-prediction
```

---

## Typical Workflow

```bash
# 1. Start fresh from main
git checkout main
git pull origin main

# 2. Create your branch
git checkout -b phase2/baseline-models

# 3. Work, save files, run notebook

# 4. Stage and commit
git add notebooks/phase2_baseline/02_baseline_logistic.ipynb
git commit -m "add logistic regression baseline with L1/L2"

# 5. Push
git push -u origin phase2/baseline-models

# 6. Open a Pull Request on GitHub → request review from a teammate
```

---

## Questions?

Post in the team group chat or open a GitHub Issue tagged with the phase label.
