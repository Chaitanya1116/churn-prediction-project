import pandas as pd

def load_and_clean_data(path):
    df = pd.read_excel('../Data/online_retail_II.xlsx')

    df = df.dropna(subset=['Customer ID'])
    df = df.drop_duplicates()

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Customer ID'] = df['Customer ID'].astype(int)

    df['TotalPrice'] = df['Quantity'] * df['Price']

    return df