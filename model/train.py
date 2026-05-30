from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import joblib
import os
import re
import pandas as pd

df = pd.read_csv(r"data\processed\mizan_dataset.csv")
arabic_df = df[df["language"] == "ar"]
english_df = df[df["language"] == "en"]


def clean_arabic(text):
    text = re.sub(r"[\u0617-\u061A\u064B-\u065F]", "", text)


def train_pipeline(df, language):
    x = df["text"]
    y = df["label"]
    X_train, X_test, Y_train, Y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )
    df["text"] = df["text"].apply(clean_arabic)
    vectorizer = TfidfVectorizer(max_features=5000)
    x_train_vec = vectorizer.fit_transform(X_train)
    x_test_vec = vectorizer.transform(X_test)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(x_train_vec, Y_train)
    y_pred = knn.predict(x_test_vec)
    print(f"\n--- {language.upper()} Model ---")
    print(classification_report(Y_test, y_pred))
    os.makedirs("model/artifacts", exist_ok=True)
    joblib.dump(vectorizer, f"model/artifacts/{language}_vectorizer.joblib")
    joblib.dump(knn, f"model/artifacts/{language}_knn.joblib")
    print(f"Saved {language} model artifacts.")
    pass


train_pipeline(arabic_df, "ar")
train_pipeline(english_df, "en")
