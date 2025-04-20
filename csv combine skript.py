# Script für zusamensetzung mehrere .CSV Dateien.
# Man braucht es für bessere datenbearbeitung bei D3 visualisierungen:
# BSP: "Dot Plots D3 another.html" und Datensatz: "DE_daily_combines.csv"

import pandas as pd


files = ["DE_2021_daily.csv", "DE_2022_daily.csv", "DE_2023_daily.csv", "DE_2024_daily.csv"]

df_list = [pd.read_csv(file) for file in files]

# Zu einem großen DataFrame zusammenfügen
df = pd.concat(df_list, ignore_index=True)


df["Datetime (UTC)"] = pd.to_datetime(df["Datetime (UTC)"])

df["Year"] = df["Datetime (UTC)"].dt.year
df["DayOfYear"] = df["Datetime (UTC)"].dt.dayofyear


df = df[["Datetime (UTC)", "Carbon Intensity gCO₂eq/kWh (direct)", "Year", "DayOfYear"]]

df.to_csv("DE_daily_combined.csv", index=False)

print("✅ Datei erfolgreich erstellt: DE_daily_combined.csv")
