import pandas as pd 
file = input("CSV file name: ")
col = input("Review text column: ")
df =pd.read_csv(file)
print("Rows at start:",len(df))
df=df.dropna(subset=[col])
print("After removing blank review:",len(df))
df =df.drop_duplicates(subset=[col])
print("After removing duplicates: ",len(df))

df[col]=df[col].astype(str).str.strip()
df= df[df[col].str.split().str.len() >=3]
print("After removing very short reviews:",len(df))
print()
print("Label column values:")
print(df["label"].value_counts().head())
print()
print("Five random reviews:")
for r in df[col].sample(5,random_state=1):
    print("-",r)

df.to_csv("clean_reviews.csv",index=False)
print("Save clean_reviews.csv with", len(df),"reviews")
