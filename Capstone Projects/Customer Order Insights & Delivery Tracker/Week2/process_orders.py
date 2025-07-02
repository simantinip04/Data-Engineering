import pandas as pd
import numpy as np

df = pd.read_csv("orders.csv")

df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days

df['delayed'] = np.where(df['delay_days'] > 0, 1, 0)

df['delayed'] = df['delayed'].fillna(0).astype(int)
df['delay_days'] = df['delay_days'].fillna(0).astype(int)

df['issue'] = df['issue'].fillna('No issue')

csv_form = df.to_csv("cleaned_orders.csv", index=False)
print(csv_form)

print("\n🔸 Delay Summary by Customer:")
print(df.groupby(['customer_id', 'customer_name'])['delayed'].sum().sort_values(ascending=False))

print("\n🔸 Most Common Delivery Issues:")
print(df['issue'].value_counts())
