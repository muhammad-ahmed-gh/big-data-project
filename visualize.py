import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("===============================")
print("    visualize.py is running    ")
print("===============================\n\n")

file_path = sys.argv[1]
df = pd.read_csv(file_path)

fig, axes = plt.subplots(1, 4, figsize=(35,5))

# 1. top selling products
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(20)
top_products.plot(kind='bar', ax=axes[0])
axes[0].set_title("Top Selling Products")
axes[0].set_xlabel("Product")
axes[0].set_ylabel("Total Quantity Sold")
axes[0].tick_params(axis='x', rotation=70)

# 2. most profitable products
df['Revenue'] = df['Quantity'] * df['UnitPrice']
top_revenue = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)
top_revenue.plot(kind='bar', ax=axes[1])
axes[1].set_title("Top Revenue Products")
axes[1].set_ylabel("Revenue")
axes[1].tick_params(axis='x', rotation=45)

# 3. prices histogram
axes[2].hist(df['UnitPrice'], bins=30, range=(0, 30))
axes[2].set_title("Prices Distribution")
axes[2].set_xlabel("Price")
axes[2].set_ylabel("Frequency")

# 4. correlation heatmap
corr = df[['Quantity', 'UnitPrice', 'Revenue']].corr()
sns.heatmap(corr, ax=axes[3])
axes[3].set_title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("summary_plot.png")
plt.close()
print("Image saved to the current directory")

os.system("python cluster.py data_preprocessed.csv")