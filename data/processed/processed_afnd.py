import pandas as pd

df = pd.read_csv(
    r"C:\Users\tarek\OneDrive\Desktop\Projects\CV Projects\Mizan\data\raw\afnd_flat.csv"
)

df = df.dropna(subset=["text"])
df = df.drop_duplicates(subset=["text"])
print(df.columns.tolist())

df0 = df[df["label"] == 0].sample(min(5000, len(df[df["label"] == 0])), random_state=42)
df1 = df[df["label"] == 1].sample(min(5000, len(df[df["label"] == 1])), random_state=42)
df_sampled = pd.concat([df0, df1]).reset_index(drop=True)

df_sampled = df_sampled[["text", "label"]]
df_sampled["language"] = "ar"

df_sampled.to_csv(r"data\processed\afnd_processed.csv", index=False)

print(f"Saved {len(df_sampled)} rows")
print(df_sampled["label"].value_counts())
