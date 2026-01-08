from joblib import load
import pandas as pd

model_young = load("artifacts/model_young.joblib")
model_rest = load("artifacts/model_rest.joblib")
scaler_young = load("artifacts/scaler_young.joblib")
scaler_rest = load("artifacts/scaler_rest.joblib")

def preproccess_input(input_dict):
    expected_cols = ['age', 'number_of_dependants', 'income_level', 'income_lakhs',
       'insurance_plan', 'annual_premium_amount', 'genetical_risk',
       'normalized_risk_score', 'gender_Male', 'region_Northwest',
       'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
       'bmi_category_Obesity', 'bmi_category_Overweight',
       'bmi_category_Underweight', 'smoking_status_Occasional',
       'smoking_status_Regular', 'employment_status_Salaried',
       'employment_status_Self-Employed']

    insurance_plan_encoding = {'Gold': 3,'Silver': 2,'Bronze': 1}

    df = pd.DataFrame(0, columns=expected_cols, index=[0])

def predict(input_dict):
    input_df = preproccess_input(input_dict)