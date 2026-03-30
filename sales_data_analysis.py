import pandas as pd
# Load data 
df = pd.read_csv(r"C:\Users\anooj\Downloads\sales_data.csv")
# KPIs
total_sales = df["Revenue"].sum()
total_profit = df["Profit"].sum()
order_count = df["Order_ID"].count()
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", order_count)
# Monthly trend
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.month
monthly_sales = df.groupby("Month")["Revenue"].sum()
print("\nMonthly Sales:\n", monthly_sales)
# Top products
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\nTop Products:\n", top_products)
# Region-wise sales
region_sales = df.groupby("Region")["Revenue"].sum()
print("\nRegion-wise Sales:\n", region_sales)
# Profit margin
df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100
print("\nProfit Margin:\n", df[["Product", "Profit_Margin"]])
