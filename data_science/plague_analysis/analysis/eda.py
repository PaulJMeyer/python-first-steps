import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np


# =========================
# 1. LOAD DATA
# =========================

def load_data():
    base_dir = Path(__file__).resolve().parent
    data_file = base_dir.parent / "data" / "raw" / "Historical_Pandemic_Epidemic_Dataset.csv"
    
    df = pd.read_csv(data_file)
    
    print("Data loaded successfully")
    return df

# =========================
# 2. DATA CLEANING
# =========================

def clean_data(df):
    # Beispiel: Spaltennamen vereinheitlichen
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Beispiel: Zahlen konvertieren
    if "estimated_deaths" in df.columns:
        df["estimated_deaths"] = pd.to_numeric(df["estimated_deaths"], errors="coerce")

    return df


# =========================
# 3. OVERVIEW
# =========================

def data_overview(df):
    # print("\n--- SHAPE ---")
    # print(df.shape)

    print("\n--- COLUMNS ---")
    print(df.columns)

    print("\n--- INFO ---")
    print(df.info())

    # print("\n--- DESCRIBE ---")
    # print(df.describe(include="all"))

    #print(df["geographic_spread"].describe)
    #print(df["who_classification"].describe)
    # print(df["continents_affected"].describe)



# =========================
# 4. MISSING VALUES
# =========================

def check_missing(df):
    print("\n--- MISSING VALUES ---")

    # echte NaN + String "NaN"
    missing = df.isna().sum()

    # zusätzlich Strings wie "NaN", "nan", "N/A", ""
    additional_missing = df.apply(
        lambda col: col.astype(str).str.strip().str.lower().isin(["nan", "n/a", "none", ""]).sum()
    )

    total_missing = missing + additional_missing

    print(total_missing.sort_values(ascending=False))

# =========================
# 5. Bestimmte Histogramme
# =========================

def plot_selected_histograms(df):
    columns_to_plot = ["estimated_cases", "estimated_deaths", "case_fatality_rate_pct", "economic_impact_billion_usd"]

    for col in columns_to_plot:
        if col in df.columns:
            plt.figure(figsize=(8, 4))
            sns.histplot(df[col].dropna(), bins=20)
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Count")
            plt.tight_layout()
            plt.show()


# =========================
# 6. Histogramme
# =========================

def plot_histograms(df):
    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col].dropna(), bins=20)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()

# =========================
# 7. Boxplots
# =========================

def plot_boxplots(df):
    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[col].dropna())
        plt.title(f"Boxplot of {col}")
        plt.xlabel(col)
        plt.tight_layout()
        plt.show()

# =========================
# 8. Bestimmte Boxplots
# =========================

def plot_selected_boxplots(df):
    columns_to_plot = ["estimated_deaths", "duration_years", "start_year"]

    for col in columns_to_plot:
        if col in df.columns:
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=df[col].dropna())
            plt.title(f"Boxplot of {col}")
            plt.tight_layout()
            plt.show()

# =========================
# 9. Regionale Boxplots
# =========================

def plot_region_deaths_bosplot(df):
        region_counts = df["origin_region"].value_counts()
        valid_regions = region_counts[region_counts >= 4].index
        df_filtered = df[df["origin_region"].isin(valid_regions)]
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df_filtered, x="origin_region", y="estimated_deaths")
        plt.xticks(rotation=45)
        plt.title("Estimated Deaths by Region (min 4 entries)")
        plt.tight_layout()
        plt.show()

# =========================
# 10. Daten loggen
# =========================

def add_log_features(df):
    cols = ["estimated_deaths", "estimated_cases", "economic_impact_billion_usd"]

    for col in cols:
        if col in df.columns:
            df[f"log_{col}"] = np.log1p(df[col])  # log(1+x) → verhindert Probleme mit 0

    return df

# =========================
# 11. Log Histogramme
# =========================

def plot_log_histograms(df):
    log_cols = [col for col in df.columns if col.startswith("log_")]

    for col in log_cols:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col].dropna(), bins=20)
        plt.title(f"Histogram of {col}")
        plt.tight_layout()
        plt.show()

# =========================
# 12. Log Histogramme
# =========================

def plot_log_boxplots(df):
    log_cols = [col for col in df.columns if col.startswith("log_")]

    for col in log_cols:
        plt.figure(figsize=(6,4))
        sns.boxplot(x=df[col].dropna())
        plt.title(f"Boxplot of {col}")
        plt.tight_layout()
        plt.show()


# =========================
# 13. Summarize pathogens
# =========================

def summarize_by_pathogen(df):
    df = df.loc[df["who_classification"] == "Pandemic"].copy() #filters only pandemic entries
    summary = (
            df.groupby("pathogen_name")
        .agg(
            events                  = ("event_name",                    "count"),
            total_cases             = ("estimated_cases",               "sum"),
            total_deaths            = ("estimated_deaths",              "sum"),
            total_cost_billion_usd  = ("economic_impact_billion_usd",   "sum"),
            cfr_mean                = ("case_fatality_rate_pct",        "mean"),
        )
        .round(2)
        .sort_values("total_deaths", ascending=False)
    )
    print(summary.to_string())
    return summary
    
# =========================
# 14. Plotting summary
# =========================

def plot_by_pathogen(df):
    df = df.loc[df["who_classification"] == "Pandemic"] #filters only pandemic entries
    summary = (
            df.groupby("pathogen_name")
        .agg(
            total_cases             = ("estimated_cases",               "sum"),
            total_deaths            = ("estimated_deaths",              "sum"),
            total_cost_billion_usd  = ("economic_impact_billion_usd",   "sum"),
            cfr_mean                = ("case_fatality_rate_pct",        "mean"),
        )
        .round(2)
        .sort_values("total_deaths", ascending=False)
    )    
        
    plots = [
        ("total_deaths",   "Todesfälle gesamt",        "Anzahl Tote"),
        ("total_cases", "Fälle gesamt",              "Anzahl Fälle"),
        ("total_cost_billion_usd", "Wirtschaftsschaden", "Mrd. USD"),
        ("cfr_mean",    "Mittlere Case Fatality Rate", "CFR (%)"),
    ]

    for spalte, titel, y_label in plots:
        fig, ax = plt.subplots(figsize=(12, 5))
        sns.barplot(data=summary, x="pathogen_name", y=spalte, ax=ax)
        ax.set_title(titel)
        ax.set_xlabel("")
        ax.set_ylabel(y_label)
        ax.tick_params(axis="x", rotation=45)
        plt.tight_layout()
        plt.show()


# =========================
# 15. Plot with two y-values and bars
# =========================

def plot_dual_axis(df):
    df = df.loc[df["geographic_spread"] == "Global"].copy()
    summary = df.groupby("pathogen_name").agg(
        faelle_gesamt = ("estimated_cases",             "sum"),
        CFR_mittel =    ("case_fatality_rate_pct",      "mean"),
    ).reset_index().sort_values("faelle_gesamt", ascending=False)

    pathogens = summary["pathogen_name"]
    x = np.arange(len(pathogens))
    breite = 0.35

    fig, ax1 = plt.subplots(figsize=(14, 5))
    ax2 = ax1.twinx()       # zweite Y-Achse, gleiche X-Achse

    ax1.bar(x - breite/2, summary["faelle_gesamt"], breite,
            label="Fälle", color="#4C72B0")
    ax2.bar(x + breite/2, summary["CFR_mittel"], breite,
            label="Todesrate in %", color="#DD8452")

    ax1.set_yscale("log")
    ax1.set_ylabel("Geschätzte Fälle (log-Skala)", color="#4C72B0")
    ax2.set_ylabel("Todesrate in %", color="#DD8452")
    
    ax1.tick_params(axis="y", labelcolor="#4C72B0")
    ax2.tick_params(axis="y", labelcolor="#DD8452")

    ax1.set_xticks(x)
    ax1.set_xticklabels(pathogens, rotation=45, ha="right")
    ax1.set_title("Fälle vs. Todesrate pro Pathogen")

    # Legenden beider Achsen zusammenführen
    linien1, labels1 = ax1.get_legend_handles_labels()
    linien2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(linien1 + linien2, labels1 + labels2, loc="upper right")

    plt.tight_layout()
    plt.show()

# =========================
# 16. Case fatality rate over outbreaks for same pathogen
# =========================

def plot_cfr_over_outbreaks(df):
    
    # Subtypen auf Oberbegriff mappen
    pathogen_mapping = {
        "H1N1 Influenza":  "Influenza",
        "H2N2 Influenza":  "Influenza",
        "H3N2 Influenza":  "Influenza",
        "H5N1 Influenza":  "Influenza",
        "Vibrio cholerae El Tor": "Vibrio cholerae",
    }
    df = df.copy()
    df = df[df["pathogen_name"] != "Unknown"].copy()
    df["pathogen_gruppe"] = df["pathogen_name"].replace(pathogen_mapping)
    # Pathogens ohne Mapping behalten ihren ursprünglichen Namen
    
    # X-Achsen-Beschriftung: event_name + start_year
    df["event_label"] = df["pathogen_name"] + "\n" + df["event_name"] + "\n(" + df["start_year"].astype(str) + ")"

    # Einen Plot pro Gruppe
    for gruppe, gruppe_df in df.groupby("pathogen_gruppe"):
        if len(gruppe_df) < 2:
            continue
    
        gruppe_df = gruppe_df.sort_values("start_year")
        x = np.arange(len(gruppe_df))
        breite = 0.35

        fig, ax1 = plt.subplots(figsize=(10, 5))
        ax2 = ax1.twinx()

        ax1.bar(x - breite/2, gruppe_df["estimated_cases"], breite,
                label="Geschätzte Fälle", color="#4C72B0")
        ax2.bar(x + breite/2, gruppe_df["case_fatality_rate_pct"], breite,
                label="CFR (%)", color="#DD8452")

        ax1.set_yscale("log")  # log sinnvoll da Fallzahlen stark variieren können

        ax1.set_ylabel("Geschätzte Fälle) (Log-Skala)", color="#4C72B0")
        ax2.set_ylabel("CFR (%)", color="#DD8452")
        ax1.tick_params(axis="y", labelcolor="#4C72B0")
        ax2.tick_params(axis="y", labelcolor="#DD8452")

        ax1.set_xticks(x)
        ax1.set_xticklabels(gruppe_df["event_label"], rotation=45, ha="right")
        ax1.set_title(f"CFR vs. Fälle – {gruppe}")

        linien1, labels1 = ax1.get_legend_handles_labels()
        linien2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(linien1 + linien2, labels1 + labels2, loc="upper right")

        plt.tight_layout()
        plt.show()

# =========================
# MAIN
# =========================

def main():
    df = load_data()
    df = clean_data(df)
    df = add_log_features(df)
    data_overview(df)
    #check_missing(df)
    #plot_selected_histograms(df)
    #plot_histograms(df)
    #plot_boxplots(df)
    #plot_selected_boxplots(df)
    #plot_region_deaths_bosplot(df)
    #plot_log_histograms(df)
    #plot_log_boxplots(df)
    #plot_by_pathogen(df)
    #plot_dual_axis(df)
    plot_cfr_over_outbreaks(df)
    


if __name__ == "__main__":
    main()


