from sklearn.linear_model import LinearRegression
import pandas as pd

def train_model(df):
    X = df[['hour', 'day']]
    y = df['units_sold']
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_and_save(model, df):
    X = df[['hour', 'day']]
    predictions = model.predict(X)
    df['predicted_units_sold'] = predictions
    output_df = df[['timestamp', 'store_id', 'product_id', 'predicted_units_sold']]
    
    # Save predictions to CSV
    output_df.to_csv('output/predictions.csv', index=False)
    print("\n✅ Predictions saved to output/predictions.csv")
