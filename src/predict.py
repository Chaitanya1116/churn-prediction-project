import pandas as pd

def predict_churn(model, df):
    X = df[['total_spent','num_orders','avg_order_value','recency_days']]
    df['prediction'] = model.predict(X)
    
    df['prediction'] = df['prediction'].map({
        1: 'Churn',
        0: 'Not Churn'
    })
    
    return df