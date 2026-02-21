import joblib
import pandas as pd

# Load pipeline
pipeline = joblib.load("models/churn_pipeline.pkl")

# Example new customer (raw data format)
new_customer = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.5,
    "TotalCharges": 420.3
}

# Convert to DataFrame
df = pd.DataFrame([new_customer])

# Predict
prob = pipeline.predict_proba(df)[0][1]
prediction = int(prob > 0.35)   # use your tuned threshold

print("Churn Probability:", round(prob, 3))
print("Prediction:", "Churn" if prediction == 1 else "No Churn")