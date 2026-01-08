import streamlit as st
from predication_helper import predict
st.set_page_config(page_title="Insurance Risk Input Form", layout="wide")

st.title("Health Insurance Cost Predictor")

# ---------- ROW 1 ----------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1
    )

with col2:
    dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=6,
        value=0,
        step=1
    )

with col3:
    income_lakhs = st.number_input(
        "Income (in Lakhs)",
        min_value=0.0,
        value=10.0,
        step=0.5
    )

# ---------- ROW 2 ----------
col1, col2, col3 = st.columns(3)

with col1:
    genetic_risk = st.number_input(
        "Genetical Risk",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ['Male', 'Female']
    )

with col3:
    marital_status = st.selectbox(
        "Marital Status",
        ['Unmarried', 'Married']
    )

# ---------- ROW 3 ----------
col1, col2, col3 = st.columns(3)

with col1:
    region = st.selectbox(
        "Region",
        ['Northeast', 'Northwest', 'Southeast', 'Southwest']
    )

with col2:
    bmi_category = st.selectbox(
        "BMI Category",
        ['Overweight', 'Underweight', 'Normal', 'Obesity']
    )

with col3:
    smoking_status = st.selectbox(
        "Smoking Status",
        [
            'Regular',
            'No Smoking',
            'Occasional',
            'Smoking=0',
            'Does Not Smoke',
            'Not Smoking'
        ]
    )

# ---------- ROW 4 ----------
col1, col2, col3 = st.columns(3)

with col1:
    employment_status = st.selectbox(
        "Employment Status",
        ['Self-Employed', 'Freelancer', 'Salaried']
    )

with col2:
    income_level = st.selectbox(
        "Income Level",
        ['<10L', '10L - 25L', '25L - 40L', '> 40L']
    )

with col3:
    insurance_plan = st.selectbox(
        "Insurance Plan",
        ['Bronze', 'Silver', 'Gold']
    )

# ---------- ROW 5 ----------
col1, col2, col3 = st.columns(3)

with col1:
    medical_history = st.selectbox(
        "Medical History",
        [
            'No Disease',
            'High blood pressure',
            'Diabetes',
            'Heart disease',
            'Thyroid',
            'Diabetes & High blood pressure',
            'Diabetes & Heart disease',
            'Diabetes & Thyroid',
            'High blood pressure & Heart disease'
        ]
    )

# ---------- SUBMIT ----------
st.markdown("---")

if st.button("Submit"):
    st.subheader("Selected Inputs")

    input_data = {
        "age": age,
        "dependents": dependents,
        "income_lakhs": income_lakhs,
        "genetic_risk": genetic_risk,
        "gender": gender,
        "marital_status": marital_status,
        "region": region,
        "bmi_category": bmi_category,
        "smoking_status": smoking_status,
        "employment_status": employment_status,
        "income_level": income_level,
        "medical_history": medical_history,
        "insurance_plan": insurance_plan
    }

    predict(input_data)
