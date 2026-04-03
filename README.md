#  Data Analysis Project by Arya

##  Project Overview
This project analyzes sales data to extract meaningful insights such as revenue trends, profit performance, and regional sales distribution. It demonstrates a complete data analysis workflow from data preparation to visualization.

---

##  Tools & Technologies Used
- Excel (Data Cleaning)
- MySQL (Database Management)
- Python (Pandas for Data Analysis)
- Power BI (Dashboard Visualization)

---

##  Project Files
- `sales_data.csv` → Dataset used for analysis  
- `sales_data_analysis.py` → Python script for KPI calculation  
- `Project_Dashboard.pbix` / `.pbit` → Power BI dashboard  
- `database_setup.sql` → SQL script for database creation and analysis  

---

##  Database Setup (MySQL)

The project uses MySQL to store and manage structured sales data.

### Steps Performed:
1. Created database `sales_project`
2. Created table `sales` with relevant fields
3. Imported CSV data using `LOAD DATA INFILE`
4. Performed SQL queries for KPI analysis

### Key SQL Operations:
```sql
CREATE DATABASE sales_project;
USE sales_project;

CREATE TABLE sales (
    Order_ID INT,
    Order_Date DATE,
    Customer_ID VARCHAR(10),
    Customer_Name VARCHAR(50),
    Region VARCHAR(20),
    Product VARCHAR(50),
    Category VARCHAR(50),
    Quantity INT,
    Price INT,
    Cost INT,
    Revenue INT,
    Profit INT
);

LOAD DATA LOCAL INFILE 'sales_data.csv'
INTO TABLE sales
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

```
##  Key Insights

1. West region generates the highest overall profit and is the top-performing region.
2. Electronics category contributes the highest revenue due to high-value products like laptops and mobiles.
3. Fashion category has the highest profit margins (up to 40%+), making it highly profitable.
4. High revenue products do not always yield high profit margins (e.g., laptops vs T-shirts).
5. Repeat customers contribute significantly to overall sales performance.
6. Accessories category shows stable but moderate profit compared to other categories.

##  Conclusion

To maximize profitability, focus on high-margin fashion products while maintaining strong sales in electronics. Target repeat customers and expand in high-performing regions like the West.
