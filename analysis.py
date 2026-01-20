import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
df = pd.read_csv('swiggy_data.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 2. Preprocessing: Categorize Veg/Non-Veg
nv_keywords = ['chicken', 'egg', 'mutton', 'fish', 'prawn', 'meat', 'kebab', 'tikka']
df['Food Type'] = df['Dish Name'].apply(lambda x: 'Non-Veg' if any(kw in str(x).lower() for kw in nv_keywords) else 'Veg')

# 3. Monthly Sales Trend Plot
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
monthly = df.groupby('Month')['Price (INR)'].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly, x='Month', y='Price (INR)', marker='o', color='orange')
plt.title('Monthly Sales Trend')
plt.savefig('monthly_sales.png')

# 4. Sales by State
state_sales = df.groupby('State')['Price (INR)'].sum().sort_values(ascending=False).head(10).reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(data=state_sales, x='Price (INR)', y='State', palette='viridis')
plt.title('Top 10 States by Sales')
plt.savefig('state_sales.png')

print("Analysis Complete. Images saved.")