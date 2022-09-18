import pandas as pd
import sys
import os

path = os.path.join(sys.path[0], "data_buddha.csv")
# print(path)
df = pd.read_csv(path)
print(df.head)