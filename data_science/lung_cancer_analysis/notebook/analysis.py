import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.parent / "data" / "lung_cancer_dataset.csv"

print("Dataset path:", DATA_FILE)

df = pd.read_csv(DATA_FILE)

# Datenüberblick:
# print(df.head())
# print(df.shape)
# print(df.columns)
print(df.info())

#Übung 1: gibt es fehlende Werte?
# print(df.isna().sum())
# print(df.isna().sum().info())

#Übung 2: Kategorien und Antwortmöglichkeiten verstehen:
# print(df["Gender"].value_counts()) #Gender: Male/Female
# print(df["WHO_Region"].value_counts()) #Western Pacific, Europe, Americas, South-East Asia, Eastern Mediterranean, Africa
# print(df["Country"].value_counts()) 
# print(df["Smoking_Status"].value_counts()) #Never Smoked, Current Smoker, Former Smoker
# print(df["Secondhand_Smoke"].value_counts()) #No, Yes
# print(df["Family_History"].value_counts()) #No, Yes
# print(df["Occupational_Hazard"].value_counts()) #No, Yes
# print(df["Alcohol_Use"].value_counts()) #Moderate, No Alcohol, Heavy

# for column in df:
#     if type == str:
#         print(df[column].value_counts())

#Übung 3: Alter analysieren
# print(df["Age"].describe()) #30-89, mean: 60.7, std: 10.3, median: 26
# print(df["Cigarettes_Per_Day"].describe()) #0-56, mean: 7.4, std: 11.8
# print(df["Years_Smoking"].describe()) #0-59, mean: 8.2, std: 12,8
# print(df["BMI"].describe()) #16-40, mean: 26.5, std: 4
# print(df["Tumor_Size_cm"].describe()) #0.5-12, mean: 4.6, std: 2.4
# print(df["Survival_Months"].describe()) #1-109, mean: 31.2, std: 23.3

#Übung 4: Raucherprofil
# print(df["Smoking_Status"].value_counts()) #Never Smoked: 979, Current: 364, Former: 157
# print(df["Cigarettes_Per_Day"].mean()) #7.4
# print(df["Years_Smoking"].mean()) #8.2

#Übung 5: Rauchen vs Symptome:
df["Coughing_num"] = df["Coughing"].map({"Yes": 1, "No": 0})
df["Shortness_of_Breath_num"] = df["Shortness_of_Breath"].map({"Yes": 1, "No": 0})
# print(df.groupby("Smoking_Status")[["Coughing_num","Shortness_of_Breath_num"]].mean())

#Alter und Geschlecht:
# print(df.groupby("Gender")[["Age"]].describe())

#Rauchen und Geschlecht:  wie gebe ich Anteile aus?
# df["Smoking_Status_num"] = df["Smoking_Status"].map({"Current Smoker": 0, "Former Smoker": 1, "Never Smoked": 2})
# print(df.groupby("Gender")["Smoking_Status"].value_counts())
# print(pd.crosstab(df["Gender"], df["Smoking_Status_num"]))

# Symptome und Geschlecht: 
# print(df.groupby("Gender")[["Coughing_num","Shortness_of_Breath_num"]].mean())

# sns.boxplot(data=df, x="Gender", y="Age")

# plt.show()

#Rauchen und Alter:
# print(df.groupby("Smoking_Status")["Age"].mean())
# print(df.groupby("Smoking_Status")["Cigarettes_Per_Day"].mean())
# print(df.groupby("Smoking_Status")["Years_Smoking"].mean())
# print(df.groupby("Smoking_Status")[["Coughing_num","Shortness_of_Breath_num"]].mean())

#Rauchen und Symptome:
df["Chest_Pain_num"] = df["Chest_Pain"].map({"Yes": 1, "No": 0})
df["Coughing_Blood_num"] = df["Coughing_Blood"].map({"Yes": 1, "No": 0})
# df["Fatigue_num"] = df["Fatigue"].map({"Yes": 1, "No": 0})
df["Weight_Loss_num"] = df["Weight_Loss"].map({"Yes": 1, "No": 0})
# df["Wheezing_num"] = df["Wheezing"].map({"Yes": 1, "No": 0})
# df["Recurrent_Infections_num"] = df["Recurrent_Infections"].map({"Yes": 1, "No": 0})
# df["Swallowing_Difficulty_num"] = df["Swallowing_Difficulty"].map({"Yes": 1, "No": 0})
# df["Finger_Clubbing"] = df["Finger_Clubbing"].map({"Yes": 1, "No": 0})
# symptoms = ["Coughing_num", "Shortness_of_Breath_num", "Fatigue_num", "Weight_Loss_num", "Wheezing_num", "Recurrent_Infections_num", "Swallowing_Difficulty_num", "Finger_Clubbing"]
# print(df.groupby("Smoking_Status")[symptoms].mean())

#Korrelationen:
# print(df.select_dtypes(include="number").columns)     #welche columns sind numerich?
cols_to_excl = ["Diagnosis_Year", "Finger_Clubbing", "Tumor_Size_cm", "BMI"]
corr = df.drop(columns=cols_to_excl).corr(numeric_only=True)       #korrelation der Werte, die numerisch sind mit .drops -> Ausnahmen

# corr_pairs = corr.unstack()                                         #Sortierte Korrelation ohne selbstkorrelation
# corr_pairs = corr_pairs[corr_pairs != 1]
# corr_pairs = corr_pairs.sort_values(ascending=False)
# print(corr_pairs.head(20))

# print(corr_pairs)

plt.figure(figsize=(14,10))         #heatmap

sns.heatmap(
    corr,
    cmap="coolwarm",
    center=0,
    annot=False
)

plt.show()

