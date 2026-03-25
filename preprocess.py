import os
import re
import pandas as pd

df = pd.read_csv("data_raw.csv")

print(df.head())
print(df.info())
print(df.describe())


print("Missing values per column:")
print(df.isna().sum())

# duplicates
duplicates = df[df.duplicated()]
print(duplicates.head())
print(f"Number of duplicates: {duplicates.shape[0]}")
df_clean = df.drop_duplicates()
print(f"Current dataset size: {df_clean.shape[0]}\n")

# -ve quantities
negative_quantities = df_clean[df_clean['Quantity'] <= 0]
print(negative_quantities.head())
print(f"Number of negative quantities: {negative_quantities.shape[0]}")
# handling with mean
quantities_mean = df_clean[df_clean['Quantity'] > 0]['Quantity'].mean()
df_clean['Quantity'] = df_clean['Quantity'].apply(lambda x: x if x > 0 else quantities_mean)
print(f"Current number of negative values: {df_clean[df_clean['Quantity'] <= 0].shape[0]}\n")

# -ve prices
negative_prices = df_clean[df_clean['UnitPrice'] <= 0]
print(negative_prices.head())
print(f"Number of negative prices: {negative_prices.shape[0]}")
# handling with median
prices_median = df_clean[df_clean['UnitPrice'] > 0]['UnitPrice'].median()
df_clean['UnitPrice'] = df_clean['UnitPrice'].apply(lambda x: x if x > 0 else prices_median)
print(f"Current number of negative values: {df_clean[df_clean['UnitPrice'] <= 0].shape[0]}\n")

# missing customers
missing_customers = df_clean[df_clean['CustomerID'].isna()]
print(missing_customers.head())
print(f"Number of missing customers: {missing_customers.shape[0]}")
# deleting rows with missing customers
df_clean = df_clean.dropna(subset=['CustomerID'])
print(f"Current number of missing customers: {df_clean[df_clean['CustomerID'].isna()].shape[0]}\n")

# missing descriptions
missing_descriptions = df_clean[df_clean['Description'].isna()]
print(missing_descriptions.head())
print(f"Number of missing descriptions: {missing_descriptions.shape[0]}")
# putting a global constant (unknown)
df_clean['Description'] = df_clean['Description'].fillna("unknown")
print(f"Current number of missing descriptions: {df_clean[df_clean['Description'].isna()].shape[0]}\n")

# final dataset size
print(f"Current dataset size: {df_clean.shape[0]}\n")

# text (description) preprocessing
df_clean['Description'] = df_clean['Description'].str.lower()
df_clean['Description'] = df_clean['Description'].apply(lambda x: re.sub('r/[^a-z0-9 ]/', '', x))
df_clean['Description'] = df_clean['Description'].str.strip()

df_clean.to_csv("data_preprocessed.csv", index=False)

# os.system("python analytics.py data_preprocessed.csv")