df.to_csv("file.csv", index=False)
df.to_parquet("file.parquet")
df.to_json("file.json", orient="records")
