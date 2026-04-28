def create_features(df):
    customer_df = df.groupby('Customer ID').agg({
        'Invoice':'nunique',
        'Quantity':'sum',
        'TotalPrice':'sum',
        'InvoiceDate':['max','min']
    })

    customer_df.columns = ['_'.join(col) for col in customer_df.columns]

    customer_df = customer_df.rename(columns={
        'Invoice_nunique':'num_orders',
        'Quantity_sum':'total_quantity',
        'TotalPrice_sum':'total_spent',
        'InvoiceDate_max':'last_purchase',
        'InvoiceDate_min':'first_purchase'
    })

    customer_df = customer_df.reset_index()

    today = df['InvoiceDate'].max()
    customer_df['recency_days'] = (today - customer_df['last_purchase']).dt.days

    customer_df['avg_order_value'] = customer_df['total_spent'] / customer_df['num_orders']

    return customer_df