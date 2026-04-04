"""
Musterlösungen – Epidemic/Pandemic Dataset
==========================================
Datei:   data_science/plague_analysis/analysis/solutions.py
Nur zur Kontrolle – erst selbst versuchen!
"""

import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

SCRIPT_DIR = Path(__file__).parent
DATA_DIR   = SCRIPT_DIR.parent / "data" / "raw"
csv_files  = list(DATA_DIR.glob("*.csv"))
df = pd.read_csv(csv_files[0])
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


# ══════════════════════════════════════════════════════════════════════════
# BLOCK A  –  GRUPPIERUNGEN & AGGREGATIONEN
# ══════════════════════════════════════════════════════════════════════════

def loesung_a1():
    result = (
        df.groupby("pathogen_type")
        .agg(
            ausbrueche   = ("event_name",             "count"),
            cfr_mittel   = ("case_fatality_rate_pct", "mean"),
            max_tote     = ("estimated_deaths",       "max"),
        )
        .round(2)
        .sort_values("ausbrueche", ascending=False)
    )
    print("A1:\n", result.to_string())


def loesung_a2():
    pt = pd.pivot_table(
        df,
        values="event_name",
        index="era",
        columns="pathogen_type",
        aggfunc="count",
        fill_value=0
    )
    print("A2:\n", pt.to_string())
    # Inhaltlich: Welche Ären dominieren welchen Erregertyp?


def loesung_a3():
    result = (
        df.groupby("geographic_spread")
        .agg(
            tote_summe      = ("estimated_deaths",       "sum"),
            dauer_mittel    = ("duration_years",          "mean"),
            cfr_median      = ("case_fatality_rate_pct", "median"),
            pathogen_typen  = ("pathogen_type",          "nunique"),
        )
        .round(2)
    )
    print("A3:\n", result.to_string())


def loesung_a4():
    df["cfr_abweichung_vom_mittel"] = (
        df["case_fatality_rate_pct"]
        - df.groupby("pathogen_type")["case_fatality_rate_pct"].transform("mean")
    )
    print("A4:\n", df[["event_name", "pathogen_type",
                        "case_fatality_rate_pct",
                        "cfr_abweichung_vom_mittel"]].head(10).to_string())


# ══════════════════════════════════════════════════════════════════════════
# BLOCK B  –  STATISTISCHE TESTS
# ══════════════════════════════════════════════════════════════════════════

def loesung_b1():
    # a) Fälle vs. Tote
    r, p = stats.pearsonr(
        df["estimated_cases"].dropna(),
        df["estimated_deaths"].dropna()
    )
    print(f"B1a) r = {r:.3f}, p = {p:.4f}")
    print("     Signifikant:", "ja" if p < 0.05 else "nein")

    # b) Dauer vs. CFR – auf gemeinsame nicht-NaN-Zeilen beschränken
    mask = df[["duration_years", "case_fatality_rate_pct"]].notna().all(axis=1)
    r2, p2 = stats.pearsonr(
        df.loc[mask, "duration_years"],
        df.loc[mask, "case_fatality_rate_pct"]
    )
    print(f"B1b) r = {r2:.3f}, p = {p2:.4f}")
    print("     Signifikant:", "ja" if p2 < 0.05 else "nein")


def loesung_b2():
    corr = df.select_dtypes(include="number").corr()
    print("B2 – stärkste Korrelationen (ohne log-Spalten):")
    corr_clean = df.filter(regex="^(?!log_)").select_dtypes(include="number").corr()
    # Oberes Dreieck maskieren, dann sortieren
    mask = np.triu(np.ones(corr_clean.shape), k=1).astype(bool)
    pairs = (
        corr_clean.where(mask)
        .stack()
        .reset_index()
        .rename(columns={"level_0": "var1", "level_1": "var2", 0: "r"})
        .reindex(corr_clean.where(mask).stack()
                 .abs().sort_values(ascending=False).index)
        .head(5)
    )
    print(pairs.to_string(index=False))


def loesung_b3():
    # Null-Hypothese: Die mittlere CFR von viralen und bakteriellen
    # Ausbrüchen ist gleich.
    viral      = df.loc[df["pathogen_type"] == "Viral",      "case_fatality_rate_pct"].dropna()
    bakteriell = df.loc[df["pathogen_type"] == "Bacterial",  "case_fatality_rate_pct"].dropna()
    t, p = stats.ttest_ind(viral, bakteriell)
    print(f"B3) t = {t:.3f}, p = {p:.4f}")
    print("    Null-Hypothese ablehnen:", "ja" if p < 0.05 else "nein")


def loesung_b4():
    stat, p = stats.shapiro(df["estimated_deaths"].dropna())
    print(f"B4) W = {stat:.4f}, p = {p:.6f}")
    print("    Normalverteilt:", "ja" if p > 0.05 else "nein")
    print("    Begründung: Todesfälle sind rechtsschief verteilt – wenige")
    print("    Pandemien mit extrem hohen Zahlen verzerren die Verteilung stark.")


# ══════════════════════════════════════════════════════════════════════════
# BLOCK C  –  VISUALISIERUNGEN
# ══════════════════════════════════════════════════════════════════════════

def loesung_c1():
    num_df = df.filter(regex="^(?!log_)").select_dtypes(include="number")
    corr = num_df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f",
                linewidths=0.5, ax=ax)
    ax.set_title("Korrelationsmatrix (ohne log-Spalten)")
    plt.tight_layout()
    plt.show()


def loesung_c2():
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="log_estimated_cases", y="log_estimated_deaths",
        hue="pathogen_type", ax=ax, s=80
    )
    # Regressionsgerade
    mask = df[["log_estimated_cases", "log_estimated_deaths"]].notna().all(axis=1)
    x = df.loc[mask, "log_estimated_cases"]
    y = df.loc[mask, "log_estimated_deaths"]
    m, b = np.polyfit(x, y, 1)
    x_line = np.linspace(x.min(), x.max(), 100)
    ax.plot(x_line, m * x_line + b, color="gray", linestyle="--", linewidth=1)

    ax.set_title("Fälle vs. Todesfälle (log-Skala)")
    ax.set_xlabel("log(Geschätzte Fälle)")
    ax.set_ylabel("log(Geschätzte Tote)")
    plt.tight_layout()
    plt.show()


def loesung_c3():
    cols = ["log_estimated_cases", "log_estimated_deaths",
            "case_fatality_rate_pct", "duration_years", "pathogen_type"]
    sns.pairplot(df[cols].dropna(), hue="pathogen_type", plot_kws={"alpha": 0.6})
    plt.suptitle("Pairplot – Kerneigenschaften der Ausbrüche", y=1.01)
    plt.show()


def loesung_c4():
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="log_estimated_cases", y="log_estimated_deaths",
        hue="pathogen_type", ax=ax, s=80
    )
    # Top 5 nach Toten annotieren
    top5 = df.nlargest(5, "estimated_deaths")
    for _, row in top5.iterrows():
        ax.annotate(
            row["event_name"],
            xy=(row["log_estimated_cases"], row["log_estimated_deaths"]),
            xytext=(5, 5), textcoords="offset points",
            fontsize=8, color="black"
        )
    ax.set_title("Fälle vs. Todesfälle – Top 5 annotiert")
    plt.tight_layout()
    plt.show()


# ══════════════════════════════════════════════════════════════════════════
# BLOCK D  –  SQL MIT SQLITE3
# ══════════════════════════════════════════════════════════════════════════

DB_PATH = SCRIPT_DIR.parent / "data" / "plague_analysis.db"
conn = sqlite3.connect(DB_PATH)
df.to_sql("outbreaks", conn, if_exists="replace", index=False)

def loesung_d1():
    q = """
    SELECT event_name, pathogen_name, start_year, case_fatality_rate_pct
    FROM outbreaks
    WHERE case_fatality_rate_pct > 20
    ORDER BY case_fatality_rate_pct DESC
    """
    print("D1:\n", pd.read_sql(q, conn).to_string(index=False))


def loesung_d2():
    q = """
    SELECT
        pathogen_type,
        COUNT(*)                              AS ausbrueche,
        ROUND(AVG(case_fatality_rate_pct), 2) AS cfr_mittel,
        MAX(estimated_deaths)                 AS max_tote
    FROM outbreaks
    GROUP BY pathogen_type
    ORDER BY ausbrueche DESC
    """
    print("D2:\n", pd.read_sql(q, conn).to_string(index=False))


def loesung_d3():
    q = """
    SELECT event_name, start_year, who_classification, estimated_deaths
    FROM outbreaks
    WHERE start_year > 1900
      AND (who_classification = 'Pandemic' OR who_classification = 'Epidemic')
      AND estimated_deaths > 1000000
    """
    print("D3:\n", pd.read_sql(q, conn).to_string(index=False))


def loesung_d4():
    q = """
    SELECT event_name, pathogen_name, estimated_deaths
    FROM outbreaks
    WHERE estimated_deaths > (SELECT AVG(estimated_deaths) FROM outbreaks)
    ORDER BY estimated_deaths DESC
    """
    print("D4:\n", pd.read_sql(q, conn).to_string(index=False))


def loesung_d5():
    q = """
    SELECT
        CASE
            WHEN case_fatality_rate_pct < 5  THEN 'niedrig'
            WHEN case_fatality_rate_pct <= 20 THEN 'mittel'
            ELSE 'hoch'
        END AS cfr_kategorie,
        COUNT(*) AS anzahl
    FROM outbreaks
    GROUP BY cfr_kategorie
    """
    print("D5:\n", pd.read_sql(q, conn).to_string(index=False))


conn.close()


# ── Alle Lösungen ausführen ────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n── BLOCK A ──────────────────────────────")
    loesung_a1()
    loesung_a2()
    loesung_a3()
    loesung_a4()

    print("\n── BLOCK B ──────────────────────────────")
    loesung_b1()
    loesung_b2()
    loesung_b3()
    loesung_b4()

    print("\n── BLOCK C ──────────────────────────────")
    loesung_c1()
    loesung_c2()
    loesung_c3()
    loesung_c4()

    print("\n── BLOCK D ──────────────────────────────")
    loesung_d1()
    loesung_d2()
    loesung_d3()
    loesung_d4()
    loesung_d5()
