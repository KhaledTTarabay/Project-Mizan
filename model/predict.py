import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from langdetect import detect

MODEL_NAME = "KhaledTTarabay/mizan-arabertv2"
ar_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
ar_model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
ar_model.eval()

def predict(text):
    lang = detect(text)

    if lang != "ar":
        return {"label": "Unsupported", "confidence": 0.0, "certainty": "Uncertain", "language": lang}

    inputs = ar_tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        outputs = ar_model(**inputs)
    probabilities = torch.softmax(outputs.logits, dim=1)[0]
    label = torch.argmax(probabilities).item()
    confidence = round(probabilities[label].item() * 100, 1)

    label_map = {0: "Fake", 1: "Credible"}
    return {
        "label": label_map[int(label)],
        "confidence": confidence,
        "certainty": get_certainty(confidence),
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
