import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("churn_pipeline.pkl")

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("📉 Customer Churn Prediction System")
st.write("Enter customer details to predict churn risk")

# ---------- USER INPUT ----------
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Has Partner", ["Yes", "No"])
Dependents = st.selectbox("Has Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)

PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# ---------- PREDICT ----------
if st.button("Predict Churn"):
    input_data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "TechSupport": TechSupport,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }])

    probability = model.predict_proba(input_data)[0][1]
    threshold = 0.35
    prediction = "Churn" if probability >= threshold else "No Churn"

    st.subheader(f"Churn Probability: {probability:.3f}")

    # ---------- High Risk Recommendations ----------
    if prediction == "Churn":
        st.error("⚠️ High Risk Customer — Likely to Churn")

        st.markdown("### 💡 Retention Recommendations (Ranked by Impact):")
        
        recommendations = []

        # Highest impact actions
        if Contract == "Month-to-month":
            recommendations.append((0.9, "Offer a longer-term contract (1-year or 2-year) to secure retention."))
        if TechSupport == "No":
            recommendations.append((0.85, "Provide premium tech support or online security packages."))
        if OnlineSecurity == "No":
            recommendations.append((0.8, "Offer online security add-on services for peace of mind."))
        if MonthlyCharges > 80:
            recommendations.append((0.75, "Provide a promotional discount or bundle to reduce monthly cost."))
        if tenure < 12:
            recommendations.append((0.7, "Engage with onboarding or loyalty programs for new customers."))
        if PaperlessBilling == "Yes":
            recommendations.append((0.6, "Offer additional incentives or loyalty rewards for paperless billing."))

        # Default recommendation if no conditions match
        if not recommendations:
            recommendations.append((0.5, "Maintain regular engagement and monitor usage patterns."))

        # Sort recommendations by impact (descending)
        recommendations.sort(reverse=True)

        # Display recommendations
        for impact, rec in recommendations:
            st.write(f"- {rec}  _(Impact Score: {impact})_")

    else:
        st.success("✅ Customer Likely to Stay")
        st.info("Maintain regular engagement to keep satisfaction high.")