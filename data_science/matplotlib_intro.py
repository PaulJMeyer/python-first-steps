import pandas as pd
import matplotlib.pyplot as plt

data = {
    "gene": ["BRCA1", "TP53", "EGFR", "MYC"],
    "expression": [12.5, 8.3, 15.2, 6.1]
}

df = pd.DataFrame(data)

#plt.bar(df["gene"], df["expression"])
plt.xlabel("Gene")
plt.ylabel("Expression")
#plt.title("Gene Expression Levels")

#plt.show()

#Übung 1: Titel und Farbe ändern
plt.title("Gene Expression")
plt.bar(df["gene"], df["expression"], color="red")

plt.show()
