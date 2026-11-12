import pandas as pd 
df=pd.read_csv("model_errors.csv")
print(df.groupby(["model_label","human_label"]).size())