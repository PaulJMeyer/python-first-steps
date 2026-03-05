import pandas as pd
import matplotlib.pyplot as plt

seqs = [
    "ATGCGTAC",
    "GGGCCC",
    "ATATAT",
    "CGCGAT"
]

def seq_to_df(seqs):
    gc_seqs = []
    for seq in seqs:
        length = len(seq)
        C = seq.count("C")
        G = seq.count("G")
        gc_percent = (G + C) / length * 100
        gc_seqs.append(gc_percent)
    df = pd.DataFrame({"sequence":seqs, "gc content": gc_seqs})
    return df

df = seq_to_df(seqs)

df["gc content"] = df["gc content"].round(2)

plt.bar(df["sequence"], df["gc content"])
plt.xlabel("Sequence")
plt.ylabel("GC content (%)")
plt.title("GC content per sequence")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()