from src.data_cleaning import clean_data
from src.feature_engineering import add_features
from src.model_training import train_model, predict_and_save
from src.stock_alerts import stock_alerts
from src.chatbot import chatbot_response

def main():
    print("\n🚀 Loading and cleaning data...")
    df = clean_data('data/input_data.csv')
    
    print("✨ Performing feature engineering...")
    df = add_features(df)
    
    print("\n📦 Checking for low-stock alerts:")
    stock_alerts(df)
    
    print("\n💬 Running customer query bot simulation:")
    for query in df['customer_query']:
        print(f"Customer: {query}")
        print(f"Bot: {chatbot_response(query)}\n")
    
    print("📈 Training demand forecasting model...")
    model = train_model(df)

    print("🧠 Generating predictions and saving output...")
    predict_and_save(model, df)

if __name__ == "__main__":
    main()
