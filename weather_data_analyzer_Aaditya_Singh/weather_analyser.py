import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. LOAD DATA
df = pd.read_csv("forecast_data.csv")

# 2. KEEP ONLY COLUMNS WE NEED
df = df[["time", "temp_c", "humidity", "precip_mm", "state", "city"]]

# 3. CONVERT TIME TO DATETIME
df["time"] = pd.to_datetime(df["time"])

# 4. RENAME COLUMNS (JUST TO BE CLEAR)
df.columns = ["date", "temperature", "humidity", "rainfall", "state", "city"]

# 5. FILL MISSING NUMERIC VALUES WITH COLUMN MEDIAN
df = df.fillna(df.median(numeric_only=True))

# 6. ADD MONTH AND YEAR COLUMNS
df["month"] = df["date"].apply(lambda x: x.month)
df["year"] = df["date"].apply(lambda x: x.year)

# 7. SAVE CLEANED DATA
os.makedirs("data", exist_ok=True)
df.to_csv("data/cleaned_weather.csv", index=False)

# 8. BASIC NUMPY STATISTICS
print("Mean temp:", np.mean(df["temperature"]))
print("Min temp :", np.min(df["temperature"]))
print("Max temp :", np.max(df["temperature"]))
print("Std temp :", np.std(df["temperature"]))

# 9. GROUP BY MONTH FOR RAINFALL AND TEMP
monthly_rain = df.groupby("month")["rainfall"].sum()
monthly_temp = df.groupby("month")["temperature"].mean()

# make folder for plots
os.makedirs("plots", exist_ok=True)

# 10. DAILY TEMPERATURE LINE PLOT
plt.plot(df["date"], df["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Trend")
plt.tight_layout()
plt.savefig("plots/daily_temperature.png")
plt.close()

# 11. MONTHLY RAINFALL BAR CHART
monthly_rain.plot(kind="bar")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall")
plt.tight_layout()
plt.savefig("plots/monthly_rainfall.png")
plt.close()

# 12. HUMIDITY VS TEMPERATURE SCATTER
plt.scatter(df["temperature"], df["humidity"])
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity")
plt.title("Humidity vs Temperature")
plt.tight_layout()
plt.savefig("plots/humidity_vs_temp.png")
plt.close()

# 13. COMBINED FIGURE (2 SUBPLOTS)
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
monthly_temp.plot()
plt.title("Avg Monthly Temp")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")

plt.subplot(1, 2, 2)
monthly_rain.plot(kind="bar")
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")

plt.tight_layout()
plt.savefig("plots/combined_plots.png")
plt.close()

print("Done. Cleaned CSV in 'data/', plots in 'plots/'.")
