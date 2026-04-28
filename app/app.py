import streamlit as st
import pandas as pd
import pickle
import sys, os
sys.path.append(os.path.abspath('..'))


from src.data_process import load_and_clean_data
from src.feature_engineering import create_features
from src.predict import predict_churn

# Load model
model = pickle.load(open('../models/churn_model.pkl','rb'))

st.title("📊 Customer Churn Prediction (AI System)")

st.write("Upload your customer data file (Excel)")

uploaded_file = st.file_uploader("Upload Excel File", type=['xlsx'])

if uploaded_file is not None:
    
    # Load data
    df = pd.read_excel(uploaded_file)
    
    st.subheader("Raw Data")
    st.write(df)
    
    # Process data
    df = load_and_clean_data(uploaded_file)
    
    # Feature engineering
    customer_df = create_features(df)
    
    # Prediction
    result_df = predict_churn(model, customer_df)
    
    st.subheader("Prediction Results")
    st.write(result_df)
    st.subheader("Churn Distribution")
    st.bar_chart(result_df['prediction'].value_counts())

    # Download button
    csv = result_df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="Download Results",
        data=csv,
        file_name='churn_predictions.csv',
        mime='text/csv'
    )