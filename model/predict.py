import joblib
import os
from langdetect import detect

ar_vectorizer = joblib.load("model/artifacts/ar_vectorizer.joblib")
ar_knn = joblib.load("model/artifacts/ar_knn.joblib")

en_vectorizer = joblib.load("model/artifacts/en_vectorizer.joblib")
en_knn = joblib.load("model/artifacts/en_knn.joblib")


def predict(text):
    lang = detect(text)
    if lang != "ar":
        lang = "en"

    if lang == "ar":
        vectorizer = ar_vectorizer
        knn = ar_knn
    else:
        vectorizer = en_vectorizer
        knn = en_knn

    vec = vectorizer.transform([text])
    probabilities = knn.predict_proba(vec)[0]
    label = knn.predict(vec)[0]
    confidence = round(probabilities[label] * 100, 1)

    distances, indices = knn.kneighbors(vec, n_neighbors=3)
    label_map = {0: "Credible", 1: "Fake"}
    return {
        "label": label_map[int(label)],
        "confidence": float(round(probabilities[label] * 100, 1)),
        "certainty": get_certainty(float(round(probabilities[label] * 100, 1))),
        "language": lang,
    }


def get_certainty(confidence):
    if confidence >= 86:
        return "Almost Certainly"
    elif confidence >= 71:
        return "Probably"
    elif confidence >= 56:
        return "Likely"
    else:
        return "Uncertain"


if __name__ == "__main__":
    test = "Netanyahu Gets Re-elected"
    print(predict(test))
