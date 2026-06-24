# RetailMart Data Pipeline

## Project Overview

This project was developed as part of a Data Engineering assignment. The aim of the project is to build a simple ETL (Extract, Transform, Load) pipeline for retail sales data.

The pipeline reads data from CSV files, cleans the data, performs transformations, stores the processed data in a SQLite database, and generates useful business insights.

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQL
* VS Code

## Dataset Files

### sales_data.csv

Contains sales transaction details such as:

* sale_id
* store_id
* product_id
* quantity
* sale_date
* amount

### products.csv

Contains product information:

* product_id
* product_name
* category
* price

### stores.csv

Contains store details:

* store_id
* store_name
* city
* region

## Tasks Performed

* Loaded CSV files using Pandas
* Checked and handled missing values
* Removed duplicate records
* Converted data types
* Merged sales, product, and store data
* Calculated total revenue
* Performed revenue analysis by city
* Loaded cleaned data into SQLite database
* Executed SQL queries for reporting
* Added error handling using try-except
* Created a run_pipeline() function to automate the workflow

## Output

The project generates:

* Total Transactions
* Total Revenue
* Top Selling City
* Top Selling Product
* Revenue Per Store Per Day
* Top 3 Best Selling Products

## Conclusion

This project helped me understand the basic concepts of ETL pipelines, data cleaning, data transformation, SQL queries, and database integration using Python.
