import os
import sys
import pandas as pd

file_path = sys.argv[1]

# data.csv encoding isn't UTF-8
df = pd.read_csv(file_path, encoding="latin1")

df.to_csv("data_raw.csv", index=False)

os.system("python preprocess.py")