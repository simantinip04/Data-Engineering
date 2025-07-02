import pandas as pd
import numpy as np
from datetime import datetime

#Data
df = pd.read_csv("cleaned_orders.csv")

#Process delivery delays
df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
df['delayed'] = np.where(df['delay_days'] > 0, 1, 0)
df['delayed'] = df['delayed'].fillna(0).astype(int)

#Creating a delay summary
summary = df.groupby(['customer_id', 'customer_name'])['delayed'].sum().sort_values(ascending=False)
top5 = summary.head(5)

#Saving log file
with open("delay_summary_log.txt", "w") as log_file:
    log_file.write("🔸 Delay Summary (Top 5 Customers):\n")
    log_file.write(str(top5))
    log_file.write(f"\n\n✅ ETL job completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

print("✅ Delay summary log written to delay_summary_log.txt")
