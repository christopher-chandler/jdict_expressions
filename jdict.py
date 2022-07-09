import json
import glob

directory = glob.glob('jmdict_english/*')

results = list()
expressions = dict()


for file in directory:
    f = open(file,encoding="utf-8")
    data = json.load(f)
    results.extend(data)


for line in results:

    if isinstance(line[2], str):
        word_type = line[2]
        if 'exp' in word_type:
            id = line[6]
            ex_num = line[4]

            if ex_num == 1:
                expressions[id] = line
            else:
                if id not in expressions:
                    expressions[id] = line
to_csv = list()
for i in expressions:
    exp = expressions.get(i)
    deff = " ".join(exp[5])
    exp[5]=deff
    exp = exp[:-1]
    to_csv.append(exp)

import pandas as pd
to_csv.sort()
df = pd.DataFrame(to_csv)
df.to_csv("results.csv", index=False)
