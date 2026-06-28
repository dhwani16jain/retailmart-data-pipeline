# RetailMart Data Pipeline

## Overview

The **RetailMart Data Pipeline** is an end-to-end ETL (Extract, Transform, Load) project developed using **Python**, **Pandas**, **NumPy**, and **SQLite**. The pipeline processes retail sales data from multiple CSV files, performs data cleaning and transformation, stores the processed data in an SQLite database, and generates analytical reports using SQL queries.

This project demonstrates practical data engineering concepts including data ingestion, preprocessing, transformation, database integration, SQL reporting, and exception handling.

---

## Project Features

* Read data from multiple CSV files.
* Remove duplicate records.
* Handle missing values.
* Convert data into appropriate formats.
* Merge multiple datasets.
* Calculate total revenue.
* Store processed data in SQLite.
* Execute SQL queries for reporting.
* Generate business insights.
* Implement exception handling for robust execution.

---

## Technology Stack

* Python 3
* Pandas
* NumPy
* SQLite3
* SQL
* Git
* GitHub
* Visual Studio Code

---

## Project Structure

```text
RetailMart_Data_Pipeline/
│
├── retail_mart.py          # Main ETL pipeline
├── sales_data.csv          # Sales dataset
├── products.csv            # Product dataset
├── stores.csv              # Store dataset
├── retail_sales.db         # SQLite database (generated after execution)
├── README.md               # Project documentation
```

---

## ETL Workflow

```text
CSV Files
    │
    ▼
Data Ingestion
    │
    ▼
Data Cleaning
    │
    ▼
Data Transformation
    │
    ▼
SQLite Database
    │
    ▼
SQL Reporting
    │
    ▼
Business Insights
```

---

## Project Tasks

### Task 1 – Data Ingestion

* Load sales, products, and stores datasets.
* Inspect dataset structure.
* Check for missing values.

### Task 2 – Data Cleaning

* Remove duplicate records.
* Handle missing values.
* Convert data types.

### Task 3 – Data Transformation

* Merge datasets.
* Calculate total revenue.
* Generate statistical summaries.

### Task 4 – Data Loading

* Create SQLite database.
* Store processed data.
* Execute SQL queries.

### Task 5 – Reporting & Insights

* Top-selling products.
* Revenue by city.
* Revenue by store.
* Business summary report.

---

## Sample Output

```text
========================================
      RETAILMART SUMMARY REPORT
========================================
Total Transactions : 14
Total Revenue      : Rs. 8,550.00
Top Selling City   : Chennai
Top Selling Product: Cooking Oil 1L
========================================
Database connection closed.
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/dhwani16jain/RetailMart-Data-Pipeline.git
```

### 2. Navigate to the project folder

```bash
cd RetailMart-Data-Pipeline
```

### 3. Install the required libraries

```bash
pip install pandas numpy
```

### 4. Run the pipeline

```bash
python retail_mart.py
```

---

## Future Enhancements

* Integrate with MySQL or PostgreSQL.
* Build an interactive dashboard using Power BI or Streamlit.
* Automate the ETL process using Apache Airflow.
* Deploy the pipeline on cloud platforms.
* Implement logging and monitoring.


