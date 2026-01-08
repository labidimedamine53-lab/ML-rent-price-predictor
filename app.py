import numpy as np
import pandas as pd
import joblib
import streamlit as st
from pathlib import Path

# Load model bundle next to this script (robust if launched from another folder)
MODEL_PATH = Path(__file__).with_name("rent_model.joblib")
bundle = joblib.load(MODEL_PATH)

pipe = bundle["pipeline"]
FEATURES_NUM = bundle["features_num"]
FEATURES_CAT = bundle["features_cat"]
CLIP_MAX_LOG = bundle.get("clip_max_log", 10)

st.set_page_config(page_title="Rent Price Predictor", layout="centered")
st.title("Rent Price Prediction")
st.caption("Predicts monthly rent (proxy) based on listing features. Model trained in log-space.")

with st.form("rent_form"):
    col1, col2 = st.columns(2)

    with col1:
        accommodates = st.number_input("Accommodates", min_value=1, max_value=20, value=2)
        bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=1)
        bathrooms = st.number_input("Bathrooms", min_value=0.0, max_value=10.0, value=1.0, step=0.5)

    with col2:
        latitude = st.number_input("Latitude", value=44.4949, format="%.6f")
        longitude = st.number_input("Longitude", value=11.3426, format="%.6f")
        neighbourhood = st.text_input("Neighbourhood (exact label from dataset)", value="")

    submitted = st.form_submit_button("Predict")

if submitted:
    row = {
        "accommodates": accommodates,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "latitude": latitude,
        "longitude": longitude,
        FEATURES_CAT[0]: neighbourhood
    }
    X_input = pd.DataFrame([row])

    pred_log = float(pipe.predict(X_input)[0])
    pred_log = min(pred_log, CLIP_MAX_LOG)

    pred_eur = float(np.exp(pred_log))

    st.subheader("Estimated monthly rent")
    st.metric("Prediction (€ / month)", f"{pred_eur:,.0f}")

    st.caption("If the neighbourhood is unknown, the model ignores it (OneHotEncoder(handle_unknown='ignore')).")
