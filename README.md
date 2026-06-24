# Project Mizan ميزان: A Multilingual Misinformation Detector

## Manifesto

Growing up in Lebanon, I watched misinformation move faster than truth — shaping opinions, justifying hatred, swaying my country's future. Mizan is my attempt to push back. Not a fact-checker, but a mirror that asks: how confident are we in what shapes our reality, and who feeds us information?

## Live Demo

[mizan.streamlit.app](https://project-mizan.streamlit.app/)

---

## How It Works

### Mizan v2 (Current)

Mizan v2 upgrades the Arabic pipeline from a classical TF-IDF/KNN approach to a fine-tuned transformer model.

1. **Language Detection** — Input text is automatically detected using `langdetect`. Currently, only Arabic is supported in the v2 pipeline. English support is planned for v3.

2. **Arabic Pipeline (AraBERT)** — Arabic text is classified using a fine-tuned `aubmindlab/bert-base-arabertv2` model, trained on the AFND dataset. The model outputs a confidence score via softmax probabilities over two classes: Credible and Fake.

3. **Certainty Scale** — Confidence scores are mapped to human-readable certainty levels:
   - 86%+ → Almost Certainly
   - 71–85% → Probably
   - 56–70% → Likely
   - Below 56% → Uncertain

### Mizan v1 (Deprecated)

The original pipeline used TF-IDF vectorization and K-Nearest Neighbors (KNN) classification for both Arabic and English. It has been replaced for Arabic in v2 and preserved for reference.

---

## Model

The fine-tuned AraBERT model is publicly available on Hugging Face Hub:

**[KhaledTTarabay/mizan-arabertv2](https://huggingface.co/KhaledTTarabay/mizan-arabertv2)**

| Metric | v1 (TF-IDF/KNN) | v2 (AraBERT) |
|---|---|---|
| Arabic F1 Score | ~60% | 89.3% |
| Model Type | KNN | Fine-tuned Transformer |
| Training Data | Mizan subset | AFND (50k rows) |

---

## Datasets

| Dataset | Language | Size | Citation |
|---|---|---|---|
| AFND | Arabic | 606,912 articles | Khalil et al. (2022), Data in Brief, doi:10.1016/j.dib.2022.108141 |
| ISOT | English | ~45,000 articles | Ahmed et al., University of Victoria |

---

## Known Limitations

- English pipeline not yet upgraded (v3 roadmap)
- Language detection unreliable on very short text
- Model trained on AFND only — may not generalize to all Arabic dialects
- Weak supervision in AFND labels

---

## How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/KhaledTTarabay/Project-Mizan.git
   cd Project-Mizan
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

> Note: No local model training required. The AraBERT model loads automatically from Hugging Face Hub on first run.

---

## Roadmap

| Version | Status | Focus |
|---|---|---|
| v1 | Deprecated | TF-IDF/KNN baseline |
| v2 | Current | AraBERT Arabic pipeline |
| v3 | Planned | English transformer upgrade,|

---

*This README was drafted with AI assistance.*