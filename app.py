import streamlit as st
import numpy as np
import joblib


model = joblib.load("linear_model.pkl")  

# App Title
st.title("🚦 Crash Severity Prediction App")

st.header("Enter Crash Details")

bike_age = st.number_input("Bike Age", min_value=0, max_value=100, value=25)
drvr_age = st.number_input("Driver Age", min_value=0, max_value=100, value=30)

bike_sex = st.selectbox("Biker Sex", ["Male", "Female", "Unknown"])
bike_alcohol = st.selectbox("Biker Alcohol Involved?", ["Yes", "No", "Unknown"])
crash_group = st.selectbox("Crash Group", ["Bike Only", "Bike vs Vehicle", "Bike vs Pedestrian"])

# Map categorical inputs to numbers
sex_map = {"Male": 1, "Female": 0, "Unknown": 2}
alcohol_map = {"Yes": 1, "No": 0, "Unknown": 2}
crash_map = {"Bike Only": 0, "Bike vs Vehicle": 1, "Bike vs Pedestrian": 2}

if st.button("Predict Crash Severity"):
    features = np.array([[bike_age,
                          drvr_age,
                          sex_map[bike_sex],
                          alcohol_map[bike_alcohol],
                          crash_map[crash_group]]])

    prediction = model.predict(features)[0]

# Define severity labels
    severity_map = {
        0: ("🟢 Low Severity", "Everything seems mild."),
        1: ("🟡 Moderate Severity", "Moderate crash, be cautious."),
        2: ("🔴 High Severity", "Serious crash risk!"),
        3: ("⚫ Critical Severity", "Extremely dangerous crash!"),
        4: ("⚠️ Unknown/Severe", "Unknown but risky."),
        5: ("🚨 Emergency Level", "Emergency level crash!")
    }

    label, advice = severity_map.get(prediction, ("❓ Unknown", "Unable to classify."))

    st.markdown(f"### {label}")
    st.info(advice)
 
