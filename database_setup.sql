-- =========================================
-- Sales Data Analysis Project - MySQL Script
-- =========================================

-- Create Database
CREATE DATABASE sales_project;

-- Use Database
USE sales_project;

-- Create Table
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

-- Enable File Import
SET GLOBAL local_infile = 1;

-- Import CSV File
LOAD DATA LOCAL INFILE 'C:/Users/anooj/Downloads/sales_data.csv'
INTO TABLE sales
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

-- =========================================
-- KPI Analysis Queries
-- =========================================

-- Total Revenue
SELECT SUM(Revenue) AS Total_Revenue FROM sales;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit FROM sales;

-- Total Orders
SELECT COUNT(*) AS Total_Orders FROM sales;

-- Region-wise Revenue
SELECT Region, SUM(Revenue) AS Revenue_By_Region
FROM sales
GROUP BY Region;
