import pandas as pd
import numpy as np
import requests
import json

def fetch_data_from_file(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def clean_and_process_data(df):
    """
    Clean the DataFrame and calculate delays.
    """
    df = df.dropna(subset=['delivery_date'])  # Drop rows with missing delivery dates
    df['delivery_date'] = pd.to_datetime(df['delivery_date'])
    df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
    df['is_delayed'] = np.where(df['delay_days'] > 0, 1, 0)
    return df

def main():
    api_url = "https://api.sampleapis.com/fakeorders/orders"  # Replace with real API if needed

    print("Fetching data from API...")
    try:
        raw_data = fetch_data_from_file('sample_orders.json')
    except Exception as e:
        print(f"API error: {e}")
        return

    df = pd.DataFrame(raw_data)
    print("\nRaw Data:")
    print(df.head())

    df_clean = clean_and_process_data(df)

    print("\nCleaned and Processed Data:")
    print(df_clean[['order_id', 'supplier_id', 'delay_days', 'is_delayed']].head())

    df_clean.to_csv("cleaned_supply_chain_data.csv", index=False)
    print("\nSaved to cleaned_supply_chain_data.csv")

if __name__ == "__main__":
    main()
