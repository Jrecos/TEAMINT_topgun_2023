import pandas as pd

# Read the cleaned product sales data
file_path = '../product_sales_cleaned.csv'
df = pd.read_csv(file_path)

# 1. Aggregation and grouping
category_group = df.groupby('Category').agg({'Sales Amount': 'sum', 'Net Sales': 'sum'})
print(category_group)

customer_group = df.groupby('Customer ID').agg({'Sales Amount': 'sum', 'Net Sales': 'sum', 'Discount': 'mean'})
print(customer_group)

# 2. Feature scaling and normalization
min_sales = df['Sales Amount'].min()
max_sales = df['Sales Amount'].max()
df['Normalized Sales Amount'] = (df['Sales Amount'] - min_sales) / (max_sales - min_sales)

# 3. Handling categorical variables
category_dummies = pd.get_dummies(df['Category'], prefix='Category')
df = pd.concat([df, category_dummies], axis=1)

# 4. Feature selection techniques
correlation_matrix = df[['Sales Amount', 'Discount', 'Profit', 'Net Sales', 'Customer Age']].corr()
print(correlation_matrix)

# 5. Time series data handling
df['Sales Date'] = pd.to_datetime(df['Sales Date'])
df['Year'] = df['Sales Date'].dt.year
df['Month'] = df['Sales Date'].dt.month
df['Day'] = df['Sales Date'].dt.day

monthly_sales = df.groupby(['Year', 'Month'])['Sales Amount'].sum()
print(monthly_sales)
