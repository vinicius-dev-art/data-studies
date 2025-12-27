import pandas as pd

df_titanic = pd.read_csv("Titanic-Dataset.xls")

print(df_titanic.head())
print(df_titanic.describe())
print(df_titanic.isna().sum())
df_titanic["Embarked"] = df_titanic["Embarked"].fillna("Not known")
df_titanic["Cabin"] = df_titanic["Cabin"].fillna("Not known")
df_titanic = df_titanic.dropna()

df_titanic.to_csv("Titanic-Dataset-cleaned.csv", index=False)
