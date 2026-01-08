# Rent Price Prediction (ML2 Project)

This project builds a **machine learning model to predict monthly rental prices** using housing features and provides an **interactive web interface** using **Streamlit**.

The model is trained in **log-space** to handle skewed rent distributions and is packaged as a reusable artifact (`rent_model.joblib`) that powers the web app.

---

## 📌 Project Overview

- **Goal**: Predict monthly rent prices (EUR/month)
- **Approach**:
  - Feature engineering + outlier removal
  - Log-transformed regression target
  - Scikit-learn pipeline with preprocessing + Ridge regression
- **Interface**: Streamlit web app (local)
- **Status**: Fully runnable end-to-end

> ⚠️ If Airbnb data is used, rent is treated as a **proxy** for long-term rental prices. This is explicitly stated and acceptable for academic projects.

---

## 📁 Project Structure

```
ML2/
│
├── AirbnbPriceChecker_interface_ready_fixed.ipynb   # Training & evaluation notebook
├── app.py                                           # Streamlit application
├── requirements.txt                                 # Python dependencies
├── rent_model.joblib                                # Trained model (generated)
├── README.md                                        # This file
└── .gitignore
```

---

## 🧠 Model Details

- **Target**: Monthly rent (EUR/month), modeled as `log(rent)`
- **Numerical features**:
  - accommodates
  - bedrooms
  - bathrooms
  - latitude
  - longitude
- **Categorical features**:
  - neighbourhood (one-hot encoded, unknowns safely ignored)
- **Model**:
  - Ridge Regression
- **Preprocessing**:
  - StandardScaler (numerical)
  - OneHotEncoder(handle_unknown="ignore") (categorical)
- **Pipeline**:
  - Implemented using ColumnTransformer + Pipeline
- **Safety**:
  - Predictions clipped before exp() to avoid overflow

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ML2-rent-price-predictor.git
cd ML2-rent-price-predictor
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model (generate rent_model.joblib)
Open the notebook and run **all cells**:

```bash
jupyter notebook AirbnbPriceChecker_interface_ready_fixed.ipynb
```

After completion, verify that `rent_model.joblib` exists in the project folder.

---

### 4️⃣ Run the Streamlit app
```bash
python -m streamlit run app.py
```

The app will open in your browser at:
```
http://localhost:8501
```

---

## 🖥️ Streamlit Interface

The web app allows you to:
- Input apartment features
- Select or type a neighbourhood
- Visualize location on a map (optional)
- Receive:
  - Estimated monthly rent (€)
  - Optional confidence interval (if enabled)

If a neighbourhood is unknown, the model does not crash and simply ignores it.

---

## 📊 Evaluation Metrics

The notebook reports:
- R² (log-space)
- MAE (EUR/month)
- RMSE (EUR/month)

These metrics ensure the model is both statistically valid and interpretable.

---

## 🔁 Reproducibility Notes

- All preprocessing is done inside the pipeline
- No data leakage
- Notebook runs cleanly with Run All
- Streamlit app loads the model relative to app.py

---

## 📚 Technologies Used

- Python 3
- pandas, numpy
- scikit-learn
- joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

## 👤 Author

**Mohamed Amine Abidi**  
MSc Electronic Engineering – University of Bologna  

---

## 📄 License

This project is for educational purposes.
