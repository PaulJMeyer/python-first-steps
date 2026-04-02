# Blood Cell Anomaly Detection – Übungsprojekt

Dieses Projekt deckt die StackFuel Data Scientist Vorbereitungsinhalte ab:
Native Python · EDA mit Pandas & Matplotlib · SQL Basics · Statistik/Mathematik

---

## Setup

### 1. Dataset herunterladen

1. Kaggle-Account erstellen: https://www.kaggle.com
2. API-Token herunterladen: Kaggle → Account → "Create New Token" → `kaggle.json`
3. Token ablegen:
   - **Windows:** `C:\Users\<DeinName>\.kaggle\kaggle.json`
   - **Mac/Linux:** `~/.kaggle/kaggle.json`
4. Dataset herunterladen:
```bash
pip install kaggle
kaggle datasets download -d alitaqishah/blood-cell-anomaly-detection-2025 -p data/raw --unzip
```

Alternativ: Dataset manuell von https://www.kaggle.com/datasets/alitaqishah/blood-cell-anomaly-detection-2025 herunterladen und in `data/raw/` entpacken.

---

### 2. Virtuelle Umgebung einrichten

```bash
# Im Projektordner (wo diese README liegt)
python -m venv .venv

# Aktivieren:
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Dependencies installieren:
pip install -r requirements.txt

# Jupyter Kernel registrieren (damit VS Code das venv findet):
python -m ipykernel install --user --name=blood-cell-venv --display-name "Blood Cell Project"
```

---

### 3. In VS Code öffnen

1. VS Code öffnen, diesen Ordner als Workspace öffnen
2. Erweiterung **"Jupyter"** von Microsoft installieren (falls noch nicht vorhanden)
3. Notebook öffnen: `notebooks/01_eda.ipynb`
4. Oben rechts Kernel auswählen: **"Blood Cell Project"**

---

## Projektstruktur

```
blood_cell_project/
├── data/
│   └── raw/          ← Dataset kommt hierhin (nicht ins Git!)
├── notebooks/
│   ├── 01_eda.ipynb              ← Phase 1 & 2: EDA
│   ├── 02_preprocessing.ipynb   ← Phase 3: Datenvorbereitung
│   ├── 03_modeling.ipynb        ← Phase 4: Modellierung
│   └── 04_evaluation.ipynb      ← Phase 5: Auswertung & SQL
├── src/
│   └── utils.py      ← Hilfsfunktionen (wiederverwendbar)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Nächste Schritte

Notebooks in dieser Reihenfolge durcharbeiten:

1. **01_eda.ipynb** – Daten laden, Klassenverteilung, Bilder anzeigen
2. **02_preprocessing.ipynb** – Normalisierung, Train/Val-Split
3. **03_modeling.ipynb** – Baseline-Modell → Random Forest
4. **04_evaluation.ipynb** – Metriken, Confusion Matrix, SQL-Export
