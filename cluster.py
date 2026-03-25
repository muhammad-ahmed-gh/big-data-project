import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("=========================")
print("  cluster.py is running  ")
print("=========================")

file_path = sys.argv[1]
df = pd.read_csv(file_path)

df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Aggregate by customer
customer_data = df.groupby('CustomerID').agg({
    'Quantity': 'sum',
    'Revenue': 'sum'
}).reset_index()

print("Grouped data:")
print(customer_data.head())

scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_data[['Quantity', 'Revenue']])


kmeans = KMeans(n_clusters=3, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(scaled_features)


print("\n\nClusters:")
print(customer_data.groupby('Cluster')[['Quantity', 'Revenue']].mean())

cluster_counts = customer_data['Cluster'].value_counts().sort_index()

print("Writing to clusters to file...")
with open("clusters.txt", "w") as f:
    f.write("Cluster counts:\n")
    for cluster_id, count in cluster_counts.items():
        f.write(f"Cluster {cluster_id}: {count}\n")

print("Workflow Finished!")