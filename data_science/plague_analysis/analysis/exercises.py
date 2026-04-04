"""
Übungsaufgaben – Epidemic/Pandemic Dataset
==========================================
Datei:   data_science/plague_analysis/analysis/exercises.py
Ausführen (im Projektroot, venv aktiv):
    python data_science/plague_analysis/analysis/exercises.py

Arbeite die Aufgaben der Reihe nach durch.
Schreibe deinen Code direkt unterhalb des jeweiligen Kommentars.
"""

import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


# ── Daten laden (bereits bekannt aus eda.py) ───────────────────────────────
SCRIPT_DIR = Path(__file__).parent
DATA_DIR   = SCRIPT_DIR.parent / "data" / "raw"
csv_files  = list(DATA_DIR.glob("*.csv"))
df = pd.read_csv(csv_files[0])
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


# ══════════════════════════════════════════════════════════════════════════
# BLOCK A  –  GRUPPIERUNGEN & AGGREGATIONEN
# ══════════════════════════════════════════════════════════════════════════

# A1 ── Einstieg
# Gruppiere nach "pathogen_type" und berechne für jede Gruppe:
#   - die Anzahl der Ausbrüche
#   - den Mittelwert der case_fatality_rate_pct
#   - den Maximalwert der estimated_deaths
# Sortiere das Ergebnis absteigend nach Anzahl der Ausbrüche.


# A2 ── pivot_table
# Erstelle eine pivot_table, die zeigt:
#   - Zeilen:   era
#   - Spalten:  pathogen_type
#   - Werte:    Anzahl der Ausbrüche (aggfunc="count", values="event_name")
# Tipp: fehlende Kombinationen mit fill_value=0 auffüllen.
# Was fällt dir inhaltlich auf?


# A3 ── Mehrere Aggregationen auf einmal
# Gruppiere nach "geographic_spread" und berechne mit .agg():
#   - Summe von estimated_deaths
#   - Mittelwert von duration_years
#   - Median von case_fatality_rate_pct
#   - Anzahl einzigartiger pathogen_type-Werte (aggfunc: "nunique")


# A4 ── Weiterführend: groupby + transform
# Füge dem DataFrame eine neue Spalte "cfr_abweichung_vom_mittel" hinzu.
# Sie soll für jede Zeile angeben, um wie viel Prozentpunkte die CFR dieser
# Zeile vom Mittelwert ihrer pathogen_type-Gruppe abweicht.
# Tipp: df.groupby(...)["..."].transform("mean")


# ══════════════════════════════════════════════════════════════════════════
# BLOCK B  –  STATISTISCHE TESTS
# ══════════════════════════════════════════════════════════════════════════

# B1 ── Korrelation
# Berechne die Pearson-Korrelation zwischen:
#   a) estimated_cases und estimated_deaths
#   b) duration_years und case_fatality_rate_pct
# Nutze scipy.stats.pearsonr() – es gibt zwei Rückgabewerte: (r, p_wert).
# Interpretiere das Ergebnis: Ist der Zusammenhang statistisch signifikant?
# (Faustregel: p < 0.05 gilt als signifikant)


# B2 ── Korrelationsmatrix
# Berechne die Korrelationsmatrix für alle numerischen Spalten mit .corr().
# Welche zwei Variablen korrelieren am stärksten (abgesehen von log-Spalten
# mit ihren Originalwerten)?


# B3 ── t-Test
# Teste, ob sich die mittlere case_fatality_rate_pct zwischen
# "viral" und "bakteriell" signifikant unterscheidet.
# Tipp: scipy.stats.ttest_ind(gruppe_a, gruppe_b)
# Formuliere eine Null-Hypothese und interpretiere das Ergebnis.


# B4 ── Weiterführend: Normalverteilung prüfen
# Prüfe mit dem Shapiro-Wilk-Test, ob estimated_deaths normalverteilt ist.
# Tipp: scipy.stats.shapiro()
# Erwarte keine Normalverteilung – begründe, warum das bei diesem Merkmal
# kaum zu erwarten ist.


# ══════════════════════════════════════════════════════════════════════════
# BLOCK C  –  VISUALISIERUNGEN
# ══════════════════════════════════════════════════════════════════════════

# C1 ── Heatmap der Korrelationsmatrix
# Visualisiere die Korrelationsmatrix aus B2 als Heatmap mit seaborn.
# Tipp: sns.heatmap(..., annot=True, cmap="coolwarm", fmt=".2f")
# Schließe die log_-Spalten aus, damit die Heatmap übersichtlich bleibt.
# Tipp: df.filter(regex="^(?!log_)") wählt alle Spalten ohne "log_"-Präfix.


# C2 ── Scatterplot
# Erstelle einen Scatterplot: x = log_estimated_cases, y = log_estimated_deaths.
# Färbe die Punkte nach "pathogen_type" ein (hue-Parameter).
# Füge mit sns.regplot() oder ax.axline() eine Regressionsgerade hinzu.
# Was sagt die Lage der Punkte relativ zur Geraden inhaltlich aus?


# C3 ── Pairplot
# Erstelle einen Pairplot für folgende Spalten:
#   log_estimated_cases, log_estimated_deaths,
#   case_fatality_rate_pct, duration_years
# Färbe nach "pathogen_type" ein.
# Tipp: sns.pairplot(df[cols], hue="pathogen_type")
# Welche Beziehung zwischen den Variablen ist am auffälligsten?


# C4 ── Weiterführend: Annotierter Scatterplot
# Baue C2 weiter aus: Beschrifte die 5 Ausbrüche mit den meisten Toten
# direkt im Plot mit ihrem event_name.
# Tipp: ax.annotate("text", xy=(x_wert, y_wert))


# ══════════════════════════════════════════════════════════════════════════
# BLOCK D  –  SQL MIT SQLITE3
# ══════════════════════════════════════════════════════════════════════════

# Setup: DataFrame in SQLite-Datenbank schreiben
DB_PATH = SCRIPT_DIR.parent / "data" / "plague_analysis.db"
conn = sqlite3.connect(DB_PATH)
df.to_sql("outbreaks", conn, if_exists="replace", index=False)
print("Datenbank erstellt:", DB_PATH)

# D1 ── SELECT + WHERE
# Schreibe eine SQL-Abfrage, die alle Ausbrüche zurückgibt,
# bei denen die case_fatality_rate_pct über 20% liegt.
# Zeige nur: event_name, pathogen_name, start_year, case_fatality_rate_pct
# Sortiere absteigend nach CFR.

query_d1 = """

"""
# print(pd.read_sql(query_d1, conn))


# D2 ── GROUP BY + Aggregation
# Schreibe eine Abfrage, die pro pathogen_type folgendes berechnet:
#   - Anzahl Ausbrüche (COUNT)
#   - Durchschnittliche CFR (AVG), gerundet auf 2 Dezimalstellen
#   - Maximale estimated_deaths (MAX)
# Sortiere nach Anzahl Ausbrüche absteigend.

query_d2 = """

"""
# print(pd.read_sql(query_d2, conn))


# D3 ── WHERE + AND / OR
# Finde alle Ausbrüche, die:
#   - nach 1900 begannen UND
#   - entweder "Pandemic" oder "Epidemic" als who_classification haben UND
#   - mehr als 1.000.000 estimated_deaths hatten
# Zeige event_name, start_year, who_classification, estimated_deaths.

query_d3 = """

"""
# print(pd.read_sql(query_d3, conn))


# D4 ── Subquery
# Finde alle Ausbrüche, deren estimated_deaths über dem
# Durchschnitt aller Ausbrüche liegt.
# Tipp: WHERE estimated_deaths > (SELECT AVG(...) FROM ...)

query_d4 = """

"""
# print(pd.read_sql(query_d4, conn))


# D5 ── Weiterführend: CASE WHEN
# Erstelle eine Abfrage, die eine neue Spalte "cfr_kategorie" erzeugt:
#   - "niedrig"   wenn CFR < 5%
#   - "mittel"    wenn CFR zwischen 5% und 20%
#   - "hoch"      wenn CFR > 20%
# Zähle dann, wie viele Ausbrüche in jede Kategorie fallen.
# Tipp: CASE WHEN ... THEN ... WHEN ... THEN ... ELSE ... END

query_d5 = """

"""
# print(pd.read_sql(query_d5, conn))


conn.close()
