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

    # print("\n--- INFO ---")
    # print(df.info())

    # print("\n--- DESCRIBE ---")
    # print(df.describe(include="all"))

    # print(df["geographic_spread"].describe)
    # print(df["origin_region"].describe)
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
# MAIN
# =========================

def main():
    df = load_data()
    df = clean_data(df)
    df = add_log_features(df)
    data_overview(df)
    #check_missing(df)
    plot_selected_histograms(df)
    #plot_histograms(df)
    #plot_boxplots(df)
    #plot_selected_boxplots(df)
    #plot_region_deaths_bosplot(df)
    plot_log_histograms(df)
    #plot_log_boxplots(df)


if __name__ == "__main__":
    main()


