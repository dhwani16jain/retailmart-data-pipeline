#===========================================
#         TASK 1:Data Ingestion
#===========================================
#testing

import pandas as pd
import numpy as np
import sqlite3

# Load all three CSV files
sales_df = pd.read_csv('sales_data.csv')
products_df = pd.read_csv('products.csv')
stores_df = pd.read_csv('stores.csv')

# Inspect each file
print('=== SALES DATA ===')
print('Shape:', sales_df.shape)   # e.g. (17, 6) = 17 rows, 6 columns
print(sales_df.head(5))

print('\n=== PRODUCTS DATA ===')
print('Shape:', products_df.shape)
print(products_df.head(5))

print('\n=== STORES DATA ===')
print('Shape:', stores_df.shape)
print(stores_df.head(5))

# Check missing values in each DataFrame
print('\n=== MISSING VALUES IN SALES DATA ===')
print(sales_df.isnull().sum())

print('\n=== MISSING VALUES IN PRODUCTS DATA ===')
print(products_df.isnull().sum())

print('\n=== MISSING VALUES IN STORES DATA ===')
print(stores_df.isnull().sum())

#===========================================
#           TASK 2:Data Cleaning
#===========================================
# Count duplicates before removing
num_duplicates = sales_df.duplicated().sum()
print(f'Duplicates found: {num_duplicates}')

# Remove duplicates, keeping the first occurrence
sales_df = sales_df.drop_duplicates()

print(f'Duplicates removed: {num_duplicates}')
print(f'New shape after removing duplicates: {sales_df.shape}')

# Fill missing 'quantity' values with 0
sales_df['quantity'] = sales_df['quantity'].fillna(0)

# Drop rows where 'amount' is missing
sales_df = sales_df.dropna(subset=['amount'])

# Print the cleaned shape
print(f'Cleaned sales data shape: {sales_df.shape}')
print("\nCleaned Sales Data:")
print(sales_df.head())

# Convert sale_date to proper datetime format
sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])

# Convert amount to float (decimal number)
sales_df['amount'] = sales_df['amount'].astype(float)

# Verify the types are correct
print(sales_df.dtypes)


#===========================================
#       TASK 3: Data Transformation
#===========================================

# First, merge sales with products on 'product_id'
merged_df = pd.merge(sales_df, products_df, on='product_id', how='left')

# Then, merge result with stores on 'store_id'
merged_df = pd.merge(merged_df, stores_df, on='store_id', how='left')

# Print the final merged DataFrame
print('=== FINAL MERGED DATAFRAME ===')
print(merged_df.shape)
print("\nFirst 10 rows of merged dataframe:")
print(merged_df.head(10))
print(merged_df.columns.tolist())  

# Add a new column: total_revenue = quantity sold x unit price
merged_df['total_revenue'] = merged_df['quantity'] * merged_df['price']

# Use NumPy to calculate statistics
print(f'Mean total_revenue:  {np.mean(merged_df["total_revenue"]):.2f}')
print(f'Max  total_revenue:  {np.max(merged_df["total_revenue"]):.2f}')
print(f'Min  total_revenue:  {np.min(merged_df["total_revenue"]):.2f}')

# Group by city and sum total_revenue
city_revenue = merged_df.groupby('city')['total_revenue'].sum()

# Sort from highest to lowest
city_revenue = city_revenue.sort_values(ascending=False)

print('=== TOTAL REVENUE BY CITY ===')
print(city_revenue)

#===========================================
#       TASK 4: Data Loading (SQL)
#===========================================

# Connect to (or create) a database file
conn = sqlite3.connect('retail_sales.db')

# Write the DataFrame to a table called 'retail_sales'
# if_exists='replace' means: drop & recreate the table each time
merged_df.to_sql('retail_sales', conn, if_exists='replace', index=False)

print('Data loaded into retail_sales.db successfully!')
print(f'Total rows inserted: {len(merged_df)}')

# Write the SQL query
query = '''
    SELECT 
        product_name,
        SUM(quantity) AS total_quantity_sold
    FROM retail_sales
    GROUP BY product_name
    ORDER BY total_quantity_sold DESC
    LIMIT 3;
'''

# Run the query and load results into a DataFrame
top_products = pd.read_sql_query(query, conn)

print('=== TOP 3 BEST SELLING PRODUCTS ===')
print(top_products)


#===========================================
#       TASK 5: Reporting & Insights
#===========================================

query2 = '''
    SELECT
        store_name,
        sale_date,
        SUM(total_revenue) AS daily_revenue
    FROM retail_sales
    GROUP BY store_name, sale_date
    ORDER BY store_name, sale_date;
'''

store_daily = pd.read_sql_query(query2, conn)
print('=== REVENUE PER STORE PER DAY ===')
print(store_daily)

# Total transactions
total_transactions = len(merged_df)

# Total revenue
total_revenue = merged_df['total_revenue'].sum()

# Top selling city (most revenue)
top_city = merged_df.groupby('city')['total_revenue'].sum().idxmax()

# Top selling product (most quantity)
top_product = merged_df.groupby('product_name')['quantity'].sum().idxmax()

print('=' * 40)
print('      RETAILMART SUMMARY REPORT')
print('=' * 40)
print(f'Total Transactions : {total_transactions}')
print(f'Total Revenue      : Rs. {total_revenue:,.2f}')
print(f'Top Selling City   : {top_city}')
print(f'Top Selling Product: {top_product}')
print('=' * 40)
conn.close()