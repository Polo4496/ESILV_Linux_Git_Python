import pandas as pd
import numpy as np

df = pd.read_csv('avax_data.csv', names=["Date", "Price"])
df['Date'] = pd.to_datetime(df['Date'])
df["Price"] = pd.to_numeric(df["Price"], errors='coerce')

last_date = df['Date'].max().date()
last_day_data = df[df['Date'].dt.date == last_date].reset_index()
last_day_data.drop('index', axis=1, inplace=True)
pct_change = last_day_data['Price'].pct_change()
return_last_day = (1 + pct_change).cumprod().iloc[-1] - 1
volatility_last_day = pct_change.std() * (252**0.5)

max_last_day = max(last_day_data["Price"])
min_last_day = min(last_day_data["Price"])
mean_last_day = last_day_data["Price"].mean()
open_last_day = last_day_data["Price"][0]
close_last_day = np.array(last_day_data["Price"])[-1]

data_report = pd.DataFrame(columns=["Date", "Return", "Vol", "Max", "Min", "Mean", "Open", "Close"])
data_report.loc[0]=[last_date, return_last_day, volatility_last_day, max_last_day, min_last_day, mean_last_day, open_last_day, close_last_day]
data_report.to_csv("report.csv")
