import streamlit as st
import numpy as np
import joblib

# Load the trained XGBoost model
model = joblib.load("model_XGBoost.pkl")

# Initialize session state
if "predicted" not in st.session_state:
    st.session_state.predicted = False
if "result" not in st.session_state:
    st.session_state.result = None

st.title("📈 Student Social Media Addiction Predictor (XGBoost)")
st.markdown(
    "Enter the student's details to predict if they are addicted to social media."
)


# Reset function
def reset_form():
    st.session_state.predicted = False
    st.session_state.result = None
    st.rerun()


# Show the form if no prediction yet
if not st.session_state.predicted:
    gender = st.selectbox("Gender", ["Male", "Female"])
    academic_level = st.selectbox(
        "Academic Level", ["High School", "Undergraduate", "Graduate"]
    )
    avg_daily_usage = st.slider("Average Daily Usage (hours)", 0.0, 12.0, 2.0, step=0.1)
    affects_academic = st.selectbox("Affects Academic Performance?", ["No", "Yes"])
    sleep_hours = st.slider("Sleep Hours Per Night", 0.0, 12.0, 6.0, step=0.5)
    mental_health = st.slider("Mental Health Score (1–10)", 1, 10, 5)
    relationship_status = st.selectbox(
        "Relationship Status", ["Single", "In a Relationship", "Other"]
    )
    conflicts = st.slider("Conflicts Over Social Media", 0, 10, 0)

    platforms = [
        "Facebook",
        "Instagram",
        "KakaoTalk",
        "LINE",
        "LinkedIn",
        "Snapchat",
        "TikTok",
        "Twitter",
        "VKontakte",
        "WeChat",
        "WhatsApp",
        "YouTube",
    ]
    most_used_platform = st.selectbox("Most Used Platform", platforms)

    # Encode input features
    gender_val = 1 if gender == "Male" else 0
    academic_val = {"High School": 1, "Undergraduate": 2, "Graduate": 3}[academic_level]
    affects_val = 1 if affects_academic == "Yes" else 0
    rel_val = {"Single": 1, "In a Relationship": 2, "Other": 3}[relationship_status]
    platform_encoded = [
        1 if platform == most_used_platform else 0 for platform in platforms
    ]

    input_features = np.array(
        [
            gender_val,
            academic_val,
            avg_daily_usage,
            affects_val,
            sleep_hours,
            mental_health,
            rel_val,
            conflicts,
        ]
        + platform_encoded
    ).reshape(1, -1)

    # Predict
    if st.button("🔍 Predict Addiction"):
        prediction = model.predict(input_features)[0]
        st.session_state.predicted = True
        st.session_state.result = prediction
        st.rerun()

# Show result and reset button
if st.session_state.predicted:
    if st.session_state.result == 1:
        st.error("⚠️ The student is likely **Addicted** to social media.")
    else:
        st.success("✅ The student is **Not Addicted** to social media.")

    if st.button("🔁 Make Another Prediction"):
        reset_form()
