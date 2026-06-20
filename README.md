# 📉 Telecom Customer Churn Prediction & Retention Intelligence

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Enabled-orange.svg)](https://scikit-learn.org/)

> An end-to-end Machine Learning web application designed to predict telecom customer churn and provide actionable retention strategies based on individual risk factors.

Deployed app Link:- https://customer-churn-analysis-sgel5lcxrzygrvsjf637co.streamlit.app

## 🎯 Business Value
In the telecom industry, acquiring a new customer is significantly more expensive than retaining an existing one. This project doesn't just predict *if* a customer will churn—it focuses on **business-centric metrics** by optimizing for **Recall** to ensure high-risk customers aren't missed. Furthermore, it empowers Customer Success teams by generating **ranked retention recommendations** tailored to each user.

## ✨ Key Features
- **Robust ML Pipeline:** Built with Scikit-Learn using `ColumnTransformer` for strict preprocessing (`StandardScaler`, `OneHotEncoder`) to prevent data leakage.
- **Business-Optimized Inference:** Uses a custom probability threshold (0.35) specifically tuned to minimize expensive False Negatives.
- **Interactive UI:** A clean, user-friendly Streamlit interface for real-time predictions.
- **Actionable Intelligence:** Recommendation engine that outputs ranked, specific retention strategies based on the customer's unique profile (e.g., incentivizing longer contracts or upselling tech support).

## 📊 Model Performance
* **Baseline Model:** Logistic Regression (`class_weight="balanced"`), threshold tuned to 0.35
* **Recall:** 90.4% — catches 338 of 374 actual churners in the test set
* **Precision:** ~44.7% — roughly 1 in 2 flagged customers is a true churn risk
* **ROC-AUC:** 0.842

*Threshold and class weighting were deliberately tuned to favor recall: in this business
context, the cost of missing a churning customer (lost revenue) is assumed to outweigh
the cost of a false positive (an unnecessary retention offer to a loyal customer).
This tradeoff means roughly half of customers flagged as "high risk" will not have
actually churned — acceptable if retention outreach is low-cost, worth revisiting if not.*

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Yogi1107/Customer-Churn-Analysis.git
cd customer-churn-app
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app locally
```bash
streamlit run app.py
```

## **Project Structure**
```
customer_churn_app/
│
├─ app.py                       # Main Streamlit application
├─ churn_pipeline.pkl           # Trained ML pipeline
├─ requirements.txt             # Python dependencies
├─ Telco_Customer_Churn.ipynb   # Analysis
├─ Telco-Customer-Churn.csv     # Data
├─ test.py                      # Sample test
└─ README.md                    # Project documentation
```

## **Dependencies**

* streamlit
* pandas
* scikit-learn
* joblib

## **Deployment**
You can deploy the app easily on Streamlit Community Cloud:
* Push your repo to GitHub.
* Log in to Streamlit Cloud and create a new app.
* Select your repository and branch, and deploy.

## **Usage**
* Select customer details (gender, contract type, services, etc.).
* Click Predict Churn.
* View churn probability and retention recommendations if the customer is high-risk.
