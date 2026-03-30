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
- `sales_analysis.py` → Python script for KPI calculation  
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
