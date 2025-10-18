import pandas as pd 
df=pd.read_csv("games.csv")
# print(df.info())
# print(df.head())
df["Team"]=df["Team"].str.strip("[]").str.replace("'","").str.replace(", ",",").str.replace( '"','')
df["Reviews"]=df["Reviews"].str.strip("[]").str.replace("'","").str.replace(", ",",").str.replace( '"','')
df["Genres"]=df["Genres"].str.strip("[]").str.replace("'","").str.replace(", ",",").str.replace( '"','')
# print(df)


def convert_to_number(x):
    if isinstance(x, str):
        x = x.strip()
        if x.endswith("K"):
            return float(x[:-1]) * 1000
        elif x.endswith("M"):
            return float(x[:-1]) * 1000000
        else:
            try:
                return float(x)
            except:
                return x
    return x


for col in ['Times Listed','Number of Reviews',"Plays", "Playing", "Backlogs", "Wishlist"]:
    df[col] = df[col].apply(convert_to_number)

# print(df.head())

for col in ['Times Listed','Number of Reviews','Plays','Playing','Backlogs','Wishlist']:
    df[col] = df[col].astype('Int64')
df["Release Date"]=pd.to_datetime(df["Release Date"],errors="coerce")

df=df.drop(columns=["Unnamed: 0.2","Unnamed: 0.1","Unnamed: 0"])

# print(df.head())


df=df.drop_duplicates()
# print(df.size)
df.to_csv("games_cleaned.csv", index=False)