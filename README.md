# 📉 Customer Churn Prediction App

This is a **Streamlit web application** to predict the likelihood of a customer churning (leaving) based on their account and service details. The app also provides **recommendations to retain high-risk customers**.

Deployed Link:- https://customer-churn-analysis-sgel5lcxrzygrvsjf637co.streamlit.app/

---

## **Features**

- Predicts **churn probability** using a trained machine learning pipeline.
- Displays **actionable retention recommendations** for high-risk customers.
- Interactive **user input forms** for customer details.
- Easy-to-deploy Streamlit app.

---

## **Getting Started**

### **1. Clone the repository**

```bash
git clone https://github.com/yourusername/customer-churn-app.git
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
