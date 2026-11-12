import pandas as pd
file = input("CSV file name: ")
df= pd.read_csv(file)

print("Rows:", len(df))
print("Columns:", list(df.columns))
print(df.head())