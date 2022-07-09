import pandas as pd


text = open("words.txt", mode="r",encoding="utf-8")
words = [i.strip() for i in text.readlines() if i.strip() != '']
res = list()
for w in words:
    res.append(w)


df = pd.DataFrame(res)

df.to_csv("words_.csv",index=False, header=False)