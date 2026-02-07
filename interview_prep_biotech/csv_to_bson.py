import pandas as pd
from bson import BSON

# 1) Read CSV
df = pd.read_csv("runs.csv")

# 2) Transform (example patterns)
df["status"] = df["status"].astype(str).str.lower().str.strip()
df["run_start"] = pd.to_datetime(df["run_start"], errors="coerce")
df["read_count"] = pd.to_numeric(df["read_count"], errors="coerce")

df = df[
    (df["status"] == "completed") &
    (df["run_start"].notna()) &
    (df["read_count"] > 0)
].copy()

df["month"] = df["run_start"].dt.to_period("M").dt.to_timestamp()

# 3) Write as BSON (one doc per row)
with open("runs_clean.bson", "wb") as f:
    for doc in df.to_dict(orient="records"):
        f.write(BSON.encode(doc))
        f.write(b"\n")
