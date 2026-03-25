import os
import sys
import pandas as pd

print("==============================")
print("     ingest.py is running     ")
print("==============================")

file_path = sys.argv[1]

# data.csv encoding isn't UTF-8
df = pd.read_csv(file_path, encoding="latin1")

df.to_csv("data_raw.csv", index=False)
print("data_raw.csv is saved\n\n\n")

os.system("python preprocess.py data_raw.csv")