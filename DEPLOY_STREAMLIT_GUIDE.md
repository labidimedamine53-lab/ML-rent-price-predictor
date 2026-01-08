# Deploy your Streamlit app online (Streamlit Community Cloud)

## What you need in a GitHub repo
Put these files in ONE repository:
- `app.py` (use the updated one with robust model loading)
- `requirements.txt`
- `rent_model.joblib` (or a script/notebook that generates it)
- Optional: `AirbnbPriceChecker_interface_ready_fixed.ipynb` (not required for deployment)

Recommended repo layout:
```
rent-predictor/
  app.py
  requirements.txt
  rent_model.joblib
```

## 1) Create a GitHub repository
- Create a new repo on GitHub (public is simplest for free deployment).
- Upload the files above.

## 2) Streamlit Community Cloud deployment
1. Go to Streamlit Community Cloud (search: "Streamlit Community Cloud").
2. Click **New app**.
3. Select your GitHub repo.
4. Set:
   - **Main file path**: `app.py`
5. Deploy.

## Notes and common issues
### A) Large model file
If `rent_model.joblib` is large, GitHub may block it.
Solutions:
- Reduce model size (keep Ridge; avoid heavy ensembles for deployment)
- Use Git LFS (advanced)
- Or generate the model during deploy (not recommended unless dataset is small/public)

### B) Python version mismatch
Streamlit Cloud selects a Python version automatically.
If you need to pin Python, add a `runtime.txt` file:
```
python-3.11
```

### C) Missing packages
If deploy fails, check the build logs and add missing packages to `requirements.txt`.

## After deploy
You will get a public URL you can share.
