# 📉 Telecom Customer Churn Prediction & Retention Intelligence

Deployed app Link:- https://customer-churn-analysis-sgel5lcxrzygrvsjf637co.streamlit.app
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Enabled-orange.svg)](https://scikit-learn.org/)

> An end-to-end Machine Learning web application designed to predict telecom customer churn and provide actionable retention strategies based on individual risk factors.

## 🎯 Business Value
In the telecom industry, acquiring a new customer is significantly more expensive than retaining an existing one. This project doesn't just predict *if* a customer will churn—it focuses on **business-centric metrics** by optimizing for **Recall** to ensure high-risk customers aren't missed. Furthermore, it empowers Customer Success teams by generating **ranked retention recommendations** tailored to each user.

## ✨ Key Features
- **Robust ML Pipeline:** Built with Scikit-Learn using `ColumnTransformer` for strict preprocessing (`StandardScaler`, `OneHotEncoder`) to prevent data leakage.
- **Business-Optimized Inference:** Uses a custom probability threshold (0.35) specifically tuned to minimize expensive False Negatives.
- **Interactive UI:** A clean, user-friendly Streamlit interface for real-time predictions.
- **Actionable Intelligence:** Recommendation engine that outputs ranked, specific retention strategies based on the customer's unique profile (e.g., incentivizing longer contracts or upselling tech support).

## 📊 Model Performance
* **Baseline Model:** Logistic Regression (with `class_weight=\"balanced\"`)
* **Recall:** ~88% *(Optimized to capture maximum churners)*
* *Note: Recall was strictly prioritized over accuracy because missing a churning customer (False Negative) costs the business significantly more than unnecessarily flagging a loyal customer (False Positive).*

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
