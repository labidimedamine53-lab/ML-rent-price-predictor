# Training notebook patch (recommended)
# Add this AFTER you fit the pipeline and compute y_pred_log on X_test.
# It stores neighbourhood labels and residual uncertainty into rent_model.joblib
# so the Streamlit UI can show a dropdown + confidence interval.

import numpy as np
import joblib

# 1) Neighbourhood dropdown values (exact labels from your data)
neighborhoods = sorted(
    df_model["neighbourhood_cleansed"].dropna().astype(str).unique().tolist()
)

# 2) Residual spread in log-space (simple uncertainty estimate)
# y_test and y_pred_log must be defined
resid_std_log = float(np.std(y_test - y_pred_log))

bundle = {
    "pipeline": pipe,
    "features_num": FEATURES_NUM,
    "features_cat": FEATURES_CAT,
    "neighborhoods": neighborhoods,
    "resid_std_log": resid_std_log,
    "target": "rent_proxy",
    "notes": "Predicts monthly rent proxy; model trained in log-space; CI based on test residual std."
}

joblib.dump(bundle, "rent_model.joblib")
print("Saved model bundle with neighborhoods + resid_std_log: rent_model.joblib")
