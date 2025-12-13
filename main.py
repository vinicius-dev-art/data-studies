import pandas as pd

df_titanic = pd.read_csv("Titanic-Dataset.xls")

print(df_titanic.head())
print(df_titanic.describe())
