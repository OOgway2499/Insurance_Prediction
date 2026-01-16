 import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("insurance_model.pkl")

st.title("🏥 Health Insurance Price Prediction")

st.markdown("Provide your details to predict insurance price.")

# Input widgets
age = st.slider("Age", 18, 100, 30)

# Label encoding assumed: Male=1, Female=0
gender = st.selectbox("Gender", ["Female", "Male"])
gender_val = 1 if gender == "Male" else 0

bmi = st.number_input("BMI (Body Mass Index)", 10.0, 50.0, 25.0)

children = st.slider("Number of Children", 0, 5, 0)

# Label encoding assumed: smoker=1, non-smoker=0
smoking_status = st.selectbox("Smoking Status", ["Non-smoker", "Smoker"])
smoker_val = 1 if smoking_status == "Smoker" else 0

# Label encoding assumed: northeast=0, northwest=1, southeast=2, southwest=3
location = st.selectbox("Location", ["northeast", "northwest", "southeast", "southwest"])
location_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
location_val = location_map[location]

# Predict button
if st.button("Predict Insurance Cost"):
    features = np.array([[age, gender_val, bmi, children, smoker_val, location_val]])
    prediction = model.predict(features)[0]
    st.success(f"Estimated Insurance Cost: ₹{round(prediction, 2)}")
