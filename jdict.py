# Standard
import json
import glob

# Pip
import pandas as pd

# Custom
# None

directory = glob.glob("jmdict_english/*")

results = list()
expressions = dict()


for file in directory:
    f = open(file, encoding="utf-8")
    data = json.load(f)
    results.extend(data)


for line in results:

    if isinstance(line[2], str):
        word_type = line[2]
        if "exp" in word_type:
            id = line[6]
            ex_num = line[4]

            if ex_num == 1:
                expressions[id] = line
            else:
                if id not in expressions:
                    expressions[id] = line

exp_to_csv = list()

for entry in expressions:
    exp = expressions.get(entry)
    definition = " ".join(exp[5])
    exp[5] = definition
    exp = exp[:-1]
    exp_to_csv.append(exp)


exp_to_csv.sort()

df = pd.DataFrame(exp_to_csv)
df.to_csv("expression_results.csv", index=False)
