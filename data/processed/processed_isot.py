import pandas as pd

true_df = pd.read_csv(r"data\raw\ISOT_True.csv")
fake_df = pd.read_csv(r"data\raw\ISOT_Fake.csv")

true_df["label"] = 0
fake_df["label"] = 1

df = pd.concat([true_df, fake_df]).reset_index(drop=True)

df = df.dropna(subset=["text"])
df = df.drop_duplicates(subset=["text"])

print(df.columns.tolist())
print(df["label"].value_counts())

df = df[["text", "label"]]
df["language"] = "en"

df.to_csv(r"data\processed\isot_processed.csv", index=False)

print(f"Saved {len(df)} rows")
