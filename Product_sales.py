import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()

# Define the number of records
num_records = 100_000

# Generate product data
product_data = {
    'Product ID': [f'P{str(i).zfill(6)}' for i in range(num_records)],
    'Product Name': [fake.catch_phrase() for _ in range(num_records)],
    'Category': [random.choice(['Electronics', 'Furniture', 'Office Supplies', 'Apparel']) for _ in range(num_records)],
    'Sub-Category': [random.choice(['A', 'B', 'C', 'D', 'E']) for _ in range(num_records)]
}

# Generate sales data
sales_data = {
    'Sales Date': [fake.date_between(start_date='-3y', end_date='today') for _ in range(num_records)],
    'Sales Amount': [round(random.uniform(10, 1000), 2) for _ in range(num_records)],
    'Discount': [round(random.uniform(0, 0.5), 2) for _ in range(num_records)],
    'Profit': [round(random.uniform(1, 500), 2) for _ in range(num_records)]
}

# Generate customer data
customer_data = {
    'Customer ID': [f'C{str(i).zfill(6)}' for i in range(num_records)],
    'Customer Name': [fake.name() for _ in range(num_records)],
    'Customer Age': [random.randint(18, 80) for _ in range(num_records)]
}

# Combine the data into a single DataFrame
product_sales_data = pd.DataFrame({**product_data, **sales_data, **customer_data})

# Save the DataFrame as a CSV file
product_sales_data.to_csv('product_sales.csv', index=False)
