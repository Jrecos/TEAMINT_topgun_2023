import sqlite3
import pandas as pd

# Read the cleaned product sales data
file_path = '../product_sales_cleaned.csv'
df = pd.read_csv(file_path)

# Connect to the SQLite database
conn = sqlite3.connect('product_sales.db')

# 1. Create tables in the SQLite database
create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    Product_ID TEXT PRIMARY KEY,
    Product_Name TEXT,
    Category TEXT,
    Sub_Category TEXT
);
'''

create_sales_table = '''
CREATE TABLE IF NOT EXISTS sales (
    Sales_ID INTEGER PRIMARY KEY,
    Product_ID TEXT,
    Sales_Date TEXT,
    Sales_Amount REAL,
    Discount REAL,
    Profit REAL,
    Net_Sales REAL,
    FOREIGN KEY (Product_ID) REFERENCES products (Product_ID)
);
'''

create_customers_table = '''
CREATE TABLE IF NOT EXISTS customers (
    Customer_ID TEXT PRIMARY KEY,
    Customer_Name TEXT,
    Customer_Age INTEGER
);
'''

conn.execute(create_products_table)
conn.execute(create_sales_table)
conn.execute(create_customers_table)

# 2. Insert data into the tables
products = df[['Product ID', 'Product Name', 'Category', 'Sub-Category']].drop_duplicates()
products.columns = ['Product_ID', 'Product_Name', 'Category', 'Sub_Category']
products.to_sql('products', conn, if_exists='append', index=False)

sales = df[['Product ID', 'Sales Date', 'Sales Amount', 'Discount', 'Profit', 'Net Sales']].reset_index().rename(columns={'index': 'Sales_ID'})
sales.columns = ['Sales_ID', 'Product_ID', 'Sales_Date', 'Sales_Amount', 'Discount', 'Profit', 'Net_Sales']
sales.to_sql('sales', conn, if_exists='append', index=False)

customers = df[['Customer ID', 'Customer Name_x', 'Customer Age']].drop_duplicates()
customers.columns = ['Customer_ID', 'Customer_Name', 'Customer_Age']
customers.to_sql('customers', conn, if_exists='append', index=False)


# 3. Reading data from the database
def get_records(table_name):
    query = f"SELECT * FROM {table_name};"
    result = pd.read_sql_query(query, conn)
    return result


def get_sales_by_date_range(start_date, end_date):
    query = f"SELECT * FROM sales WHERE Sales_Date BETWEEN '{start_date}' AND '{end_date}';"
    result = pd.read_sql_query(query, conn)
    return result


print(get_records('sales'))
print(get_sales_by_date_range('2021-01-01', '2021-03-31'))


# 4. Updating data in the database
def update_product_category(product_id, category, sub_category):
    query = f"UPDATE products SET Category = '{category}', Sub_Category = '{sub_category}' WHERE Product_ID = '{product_id}';"
    conn.execute(query)
    conn.commit()


update_product_category('P000001', 'New Category', 'New Sub-Category')


# 5. Deleting data from the database
def delete_low_net_sales(threshold):
    query = f"DELETE FROM sales WHERE Net_Sales < {threshold};"
    conn.execute(query)
    conn.commit()


delete_low_net_sales(100)

# Close the database connection
conn.close()
