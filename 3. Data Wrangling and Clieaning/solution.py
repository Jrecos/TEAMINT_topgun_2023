import pandas as pd

# 1. Importing data
file_path = '../product_sales.csv'
df = pd.read_csv(file_path)
print(df.head(10))

# 2. Data exploration
print(df.shape)
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())

# 3. Handling missing values
df['Category'].fillna('Unknown', inplace=True)
df['Sub-Category'].fillna('Unknown', inplace=True)
df.dropna(subset=['Sales Amount', 'Profit'], inplace=True)

# 4. Data type conversion
df['Sales Date'] = pd.to_datetime(df['Sales Date'])
df['Customer Age'] = df['Customer Age'].astype(int)

# 5. Filtering and sorting data
filtered_df = df[df['Discount'] > 0.1]
filtered_df = filtered_df.sort_values(by='Sales Amount', ascending=False)

# 6. Merging, joining, and concatenating data
unique_customers = df[['Customer ID', 'Customer Name']].drop_duplicates()
merged_df = pd.merge(filtered_df, unique_customers, on='Customer ID', how='left')

# 7. Applying functions to data
merged_df['Net Sales'] = merged_df['Sales Amount'] * (1 - merged_df['Discount'])
average_net_sales_per_customer = merged_df.groupby('Customer ID')['Net Sales'].mean()
print(average_net_sales_per_customer)

# Save the cleaned DataFrame as a CSV file
merged_df.to_csv('product_sales_cleaned.csv', index=False)
