import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

n = int(input("How many reviews to analyze?"))
df= pd.read_csv("clean_reviews.csv")
df= df.sample(n=min(n,len(df)),random_state=1)

def get_label(text):
    score = TextBlob(str(text)).sentiment.polarity
    if score>0.1:
        return "positive"
    elif score <-0.1:
        return "negative"
    return "neutral"

df["model_label"]=df["Review"].apply(get_label)
df["human_label"]= ""

print(df["model_label"].value_counts())

df["model_label"].value_counts().plot(kind="bar")
plt.title("Nike review sentiment (model)")
plt.show()
df.to_csv("labeled_reviews.csv",index=False)
print("Saved labeled_review.csv with",len(df),"Review")