import pandas as pd
import matplotlib.pyplot as plt

data = {
    "gene": ["A", "B", "C", "D"],
    "expression": [10, 25, 7, 15]
}

df = pd.DataFrame(data)

print(df)

plt.bar(df["gene"], df["expression"])
plt.title("Gene Expression")
plt.show()