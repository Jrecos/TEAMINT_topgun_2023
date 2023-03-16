import pandas as pd
import sqlite3


def extract(file_path):
    df = pd.read_csv(file_path)
    return df


def transform(df):
    # Calculate the total profit per category
    df_agg = df.groupby('Category').agg({'Profit': 'sum'}).reset_index()

    # Calculate the average discount per category
    df_agg['Average Discount'] = df.groupby('Category')['Discount'].mean().values

    # Rename columns
    df_agg.columns = ['Category', 'Total Profit', 'Average Discount']

    return df_agg


def load(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


file_path = '../product_sales_cleaned.csv'
db_name = 'etl_example.db'
table_name = 'category_summary'

# Perform ETL
raw_data = extract(file_path)
transformed_data = transform(raw_data)
load(transformed_data, db_name, table_name)

# Check the results
conn = sqlite3.connect(db_name)
results = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
conn.close()

print(results)
