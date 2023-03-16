import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the cleaned product sales data
file_path = '../product_sales_cleaned.csv'
df = pd.read_csv(file_path)

# 1. Bar plot of sales by category
sales_by_category = df.groupby('Category')['Sales Amount'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales Amount', data=sales_by_category)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales Amount')
plt.show()

# 2. Line plot of monthly sales
df['Sales Date'] = pd.to_datetime(df['Sales Date'])
monthly_sales = df.resample('M', on='Sales Date')['Sales Amount'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x='Sales Date', y='Sales Amount', data=monthly_sales)
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.show()

# 3. Box plot of profit by category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Profit', data=df)
plt.title('Profit Distribution by Category')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.show()

# 4. Scatter plot of sales amount vs profit
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales Amount', y='Profit', data=df)
plt.title('Sales Amount vs Profit')
plt.xlabel('Sales Amount')
plt.ylabel('Profit')
plt.show()

# 5. Heatmap of sales correlation
correlation = df[['Sales Amount', 'Discount', 'Profit', 'Customer Age']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Sales Correlation Heatmap')
plt.show()
