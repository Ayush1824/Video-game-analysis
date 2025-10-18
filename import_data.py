import pandas as pd
from sqlalchemy import create_engine

# Step 1: Read CSV from PC
df = pd.read_csv(r"games_cleaned.csv")   # apna CSV path do

# Step 2: SQL Database connection details
USER = "root"
PASSWORD = "kk1234KK"
HOST = "localhost"
DB = "video_games"

# Step 3: Create connection
engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DB}")

# Step 4: Import table into SQL
df.to_sql("games", con=engine, if_exists="replace", index=False)

print("✅ Data imported successfully into MySQL!")
