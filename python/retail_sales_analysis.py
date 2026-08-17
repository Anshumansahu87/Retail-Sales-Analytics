import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dataset/retail_sales.csv", parse_dates=["Order Date"])
df["Profit Margin"] = df["Profit"] / df["Sales"]
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

print("Rows:", len(df))
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Orders:", df["Order ID"].nunique())
print("Profit Margin:", round(df["Profit"].sum()/df["Sales"].sum()*100, 2), "%")

print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

print("\nTop 10 Products:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10))
