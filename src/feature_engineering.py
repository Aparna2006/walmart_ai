def add_features(df):
    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.dayofweek
    df['stock_status'] = df['inventory_level'].apply(lambda x: 'Low' if x < 120 else 'OK')
    return df
