import streamlit as st
import requests

# ========================
# App Title
# ========================
st.title("📊 Student Performance Prediction")

# ========================
# User Input
# ========================
st.header("Enter Student Details")

hours_studied = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)
previous_scores = st.number_input("Previous Scores", min_value=0, max_value=100, value=50)
extracurricular = st.radio("Extracurricular Activities", ["Yes", "No"])
sleep_hours = st.slider("Sleep Hours", min_value=0, max_value=12, value=6)
question_papers = st.number_input("Sample Question Papers Practiced", min_value=0, value=2)

# ========================
# Prediction Button
# ========================
if st.button("Predict Performance"):
    try:
        # Keep extracurricular as 'Yes'/'No' to match API
        extracurricular_value = "Yes" if extracurricular == "Yes" else "No"

        # Prepare data for API
        data = {
            "hours_studied": hours_studied,
            "previous_scores": previous_scores,
            "extracurricular": extracurricular_value,
            "sleep_hours": sleep_hours,
            "question_papers": question_papers
        }

        # Send POST request to Flask API
        url = "http://127.0.0.1:5000/predict"
        response = requests.post(url, json=data)

        # Display result
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"Predicted Performance Index: {prediction:.2f}")
        else:
            st.error(f"Error: {response.json().get('error')}")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
