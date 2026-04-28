# churn-prediction-project
Churn Prediction Project 
Customer Churn Prediction (AI Project)

-------------------------------------
PROJECT PURPOSE
-------------------------------------
This project predicts whether a customer will leave (churn) or stay using Machine Learning.

-------------------------------------
WHAT IS CHURN?
-------------------------------------
Churn means a customer stops using a service or product.

-------------------------------------
TECHNOLOGIES USED
-------------------------------------
- Python
- Pandas
- Scikit-learn
- Streamlit (for web application)

-------------------------------------
PROJECT STRUCTURE
-------------------------------------
churn-prediction-project/

src/         -> Data processing and ML logic
app/         -> Streamlit web application
models/      -> Saved model (churn_model.pkl)
notebooks/   -> Model training notebook
requirements.txt -> Required libraries

-------------------------------------
HOW TO RUN PROJECT (VS CODE)
-------------------------------------

STEP 1: Download Project
- Go to GitHub
- Click "Code" → "Download ZIP"
- Extract the folder

-------------------------------------

STEP 2: Open in VS Code
- Open the extracted folder in VS Code

-------------------------------------

STEP 3: Install Libraries
Open terminal and run:

pip install -r requirements.txt

-------------------------------------

STEP 4: Create Model File (IMPORTANT)

If churn_model.pkl is missing:

1. Open:
   notebooks/analysis.ipynb

2. Click "Run All"

This will create:
models/churn_model.pkl

-------------------------------------

STEP 5: Run Application

In terminal:

cd app
streamlit run app.py

-------------------------------------

STEP 6: Use Application

- App will open in browser
- Upload Excel file
- See predictions (Churn / Not Churn)

-------------------------------------

OUTPUT
-------------------------------------
- Prediction table
- Churn vs Non-churn chart

-------------------------------------

USE CASE
-------------------------------------
Helps companies identify customers likely to leave and take action.

-------------------------------------

AUTHOR
-------------------------------------
Chaitanya
