# Rent Price Prediction Project — Setup & Run Guide (Notebook + Streamlit)

This guide assumes your project folder is:

`C:\Users\Labid\Desktop\ML2`

## 1) Required files in the folder

You should have:

- `AirbnbPriceChecker_interface_ready.ipynb`
- `app.py`
- `requirements.txt`
- (generated after training) `rent_model.joblib`

## 2) One rule: NO manual scaling outside the Pipeline

Delete or ignore any cell that does manual scaling like:

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])
```

Why:
- causes `SettingWithCopyWarning`
- causes data leakage (scaler sees test data)
- breaks the interface flow

All preprocessing must be inside the scikit-learn Pipeline only.

## 3) Notebook execution order (must be followed)

1. **Imports**
2. **Load dataset** (create `df`)
3. **Feature engineering**
   - build `rent_proxy`
   - trim outliers (e.g., top 1%)
   - build `log_rent = log(rent_proxy)`
4. **Build X/y**
5. **Train/test split**
6. **Pipeline (ColumnTransformer + Ridge)**
7. **Predict + Clip + Exp**
8. **Metrics**
9. **Save model**
   - creates `rent_model.joblib` in the same folder

### Sanity checks after training
- Confirm the model file exists:
  - `rent_model.joblib` appears in the folder
- Confirm predictions are finite:
  - no `inf`, no overflow warnings

## 4) Create the model file (`rent_model.joblib`)

Open **`AirbnbPriceChecker_interface_ready.ipynb`** and run **Kernel → Restart** then **Run All**.

At the end, you should see a message confirming the model was saved (or verify the file exists).

## 5) Install dependencies (PowerShell)

Open PowerShell and run:

```powershell
cd C:\Users\Labid\Desktop\ML2
pip install -r requirements.txt
```

If `streamlit` is not found, always run it via Python:

```powershell
python -m streamlit --version
```

## 6) Run the Streamlit interface

From the same folder:

```powershell
cd C:\Users\Labid\Desktop\ML2
python -m streamlit run app.py
```

## 7) Common errors & fixes

### A) `FileNotFoundError: rent_model.joblib`
Cause: model file not created in the folder.

Fix:
1. Run the notebook **Run All** to generate it.
2. Ensure `rent_model.joblib` is next to `app.py`.

### B) `NameError: pipeline is not defined` / `y_pred_log not defined`
Cause: cells run out of order or kernel restarted.

Fix:
- Kernel → Restart
- Run All from the top.

### C) PATH warnings during install (watchmedo/streamlit not on PATH)
Not an error. Use:

```powershell
python -m streamlit run app.py
```

## 8) Recommended folder layout

```
ML2/
  AirbnbPriceChecker_interface_ready.ipynb
  app.py
  requirements.txt
  rent_model.joblib           <-- generated
  data/
    listings.csv              <-- your dataset (optional)
```

## 9) What “done” looks like

- Notebook runs with **Run All** and produces:
  - metrics (R²/MAE/RMSE)
  - `rent_model.joblib`
- Streamlit opens and returns a monthly rent prediction in €.

If anything fails, copy/paste the first traceback lines and fix incrementally.
