import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle

# =========================================================
# Load trained model and preprocessing objects
# =========================================================

# Load ANN model (no recompilation to avoid Keras issues)
model = tf.keras.models.load_model("model.h5", compile=False)

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load label encoder for Gender
with open("label_encoder_gender.pkl", "rb") as f:
    gender_encoder = pickle.load(f)

# Load one-hot encoder for Geography
with open("onehot_encoder_geo.pkl", "rb") as f:
    geo_encoder = pickle.load(f)

# =========================================================
# Streamlit UI
# =========================================================

st.set_page_config(page_title="Estimated Salary Prediction", layout="centered")

st.title("💰 Estimated Salary Prediction (ANN)")
st.write("Predict **Estimated Salary** using a trained Artificial Neural Network")

# =========================================================
# User Inputs
# =========================================================

credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
gender = st.selectbox("Gender", gender_encoder.classes_)
age = st.number_input("Age", min_value=18, max_value=100, value=35)
tenure = st.number_input("Tenure (years)", min_value=0, max_value=10, value=5)
balance = st.number_input("Balance", min_value=0.0, value=50000.0)
num_products = st.number_input("Number of Products", min_value=1, max_value=5, value=2)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active = st.selectbox("Is Active Member", [0, 1])
geography = st.selectbox("Geography", geo_encoder.categories_[0])

# =========================================================
# Prediction Logic
# =========================================================

if st.button("Predict Estimated Salary"):

    # Encode Gender
    gender_encoded = gender_encoder.transform([gender])[0]

    # Encode Geography
    geo_encoded = geo_encoder.transform([[geography]]).toarray()
    geo_df = pd.DataFrame(
        geo_encoded,
        columns=geo_encoder.get_feature_names_out(["Geography"])
    )

    # -----------------------------------------------------
    # IMPORTANT:
    # Exited MUST be included because scaler was fit with it
    # Using neutral dummy value = 0
    # -----------------------------------------------------

    input_data = pd.DataFrame([[
        credit_score,
        gender_encoded,
        age,
        tenure,
        balance,
        num_products,
        has_cr_card,
        is_active,
        0  # Exited (dummy value required for scaler compatibility)
    ]], columns=[
        "CreditScore",
        "Gender",
        "Age",
        "Tenure",
        "Balance",
        "NumOfProducts",
        "HasCrCard",
        "IsActiveMember",
        "Exited"
    ])

    # Combine numeric + geography features
    final_input = pd.concat([input_data, geo_df], axis=1)

    # Scale features
    final_input_scaled = scaler.transform(final_input)

    # Predict salary
    prediction = model.predict(final_input_scaled)
    estimated_salary = prediction[0][0]

    st.success(f"💵 Estimated Salary: ₹ {estimated_salary:,.2f}")
