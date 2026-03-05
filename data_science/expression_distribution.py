import pandas as pd
import matplotlib.pyplot as plt

expression = [12.5, 8.3, 15.2, 6.1, 10.4, 11.7, 14.3, 9.8]
bins = [6, 9, 12, 15]

df = pd.DataFrame({"expression": expression})

plt.hist(df["expression"], bins, color="red")

plt.xlabel("Expression level")
plt.ylabel("Frequency")
plt.title("Expression Distribution")

plt.show()

