import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df.columns = df.columns.str.lower().str.strip()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df
