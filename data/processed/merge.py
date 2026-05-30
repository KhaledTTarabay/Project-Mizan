import pandas as pd

arabic = pd.read_csv(r"data\processed\afnd_processed.csv")
english = pd.read_csv(r"data\processed\isot_processed.csv")

df = pd.concat([arabic, english]).reset_index(drop=True)

df = df.dropna(subset=["text"])
df = df.drop_duplicates(subset=["text"])

print(f"Total rows: {len(df)}")
print(df["language"].value_counts())
print(df["label"].value_counts())

df.to_csv(r"data\processed\mizan_dataset.csv", index=False)

print("Saved")
