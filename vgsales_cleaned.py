import pandas as pd
df=pd.read_csv("vgsales.csv")
print(df.head())
print(df.size)
df=df.drop_duplicates()