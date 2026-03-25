import sys
import pandas as pd

file_path = sys.argv[1]
df = pd.read_csv(file_path)

print("Workflow Finished!")