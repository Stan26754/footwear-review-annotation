import pandas as pd 
df = pd.read_csv("labeled_reviews.csv")
df = df.dropna(subset=["human_label"])
df["human_label"]=df["human_label"].str.strip().str.lower()

print("Review you labeled:",len(df))
print("Model accuracy:", round((df["model_label"]==df["human_label"]).mean()* 100, 1),"%")
wrong= df[df["model_label"]!=df["human_label"]]
print("Model got", len(wrong), "wrong, Here they are:")
print()
for i,row in wrong.iterrows():
    print("Model:", row["model_label"],"| You:",row["human_label"])
    print(row["Review"])
    print()
wrong.to_csv("model_errors.csv",index=False)