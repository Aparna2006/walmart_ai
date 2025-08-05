def stock_alerts(df):
    low_stock = df[df['stock_status'] == 'Low']
    for index, row in low_stock.iterrows():
        print(f"ALERT: {row['product_name']} is low in stock at Store {row['store_id']}!")
