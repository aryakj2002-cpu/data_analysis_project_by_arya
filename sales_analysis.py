import pandas as pd
df = pd.read_csv("C:/Users/anooj/Downloads/sales_cleaned.csv")
#KPIs
total_sales=df["Revenue"].sum()
total_profit=df["Profit"].sum()
order_count=df["Order_ID"].count()
print("Total Sales:",total_sales)
print("Total Profit:",total_profit)
print("Total Order:",order_count)
#Monthly trend
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
df["Month"]=df["Order_Date"].dt.month
monthly_sales=df.groupby("Month")["Revenue"].sum()
print(monthly_sales)
#Top Products
top_products=df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print(top_products)
#Region-wise sales
region_sales=df.groupby("Region")["Revenue"].sum()
print(region_sales)
#Profit margin
df["Profit_Margin"]=(df["Profit"]/df["Revenue"])*100
print(df[["Product","Profit_Margin"]])
