import pandas as pd

#Übung 1: bestimmte Daten ausgeben
data = {
    "gene": ["BRCA1", "TP53", "EGFR", "MYC"],
    "expression": [12.5, 8.3, 15.2, 6.1]
}

df = pd.DataFrame(data)

print(df)
# print(df["gene"])
# print(df["expression"])
# print(df.iloc[0])

#Übung 2: Analyse erweitern
# print(df.describe())
# print(df["expression"].mean())
# print(df["expression"].max())
# print(df["expression"].min())

#Übung 3: Daten filtern
print(df[df["expression"] > 10])

