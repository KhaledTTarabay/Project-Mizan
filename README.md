# Project Mizan: a multilingual misinformation detector

## Manifesto:

Growing up in Lebanon, I watched misinformation move faster that truth, shaping opinions, justifying hatred, swaying my country's future, Mizan is mmy attempt to push back, not a fact-check but a mirror that asks: how confident are we in what shapes our reality, and who feeds us information

## Live Demo

[mizan.streamlit.app](https://project-mizan.streamlit.app/)

## How it works:


Mizan uses a classical NLP pipeline to classify claims as credible or false

1. Language Detection Input text is automatically detected whether arabic or english using langdetect, currently all non-Arabic text defaults to english pipeline.

2. Vectorization text is converted to numerical feature vectors using Term Frequency Inverse Document Frequency (TF-IDF), Each claim becomes a vector of 5000 - 10000 weighted words score reflecting distinctive each term is across the dataset 

3. Classification A K-Nearest Neighbors (KNN) classifier finds the 5 most similar claims in the training data by vector distance and votes on the label. The confidence score reflects the vote ratio 4 out 5 fake neighbors yields 80% confidence.

Datasets 

| Dataset | Language | Size | Citation |
|---|---|---|---|
| AFND | Arabic | 606,912 articles | Khalil et al. (2022), Data in Brief, doi:10.1016/j.dib.2022.108141 |
| ISOT | English | ~45,000 articles | Ahmed et al., University of Victoria |

## Known Limitations:

- Arabic model has 60% Accuracy Rate
- Overconfident on neutral claims
- Language detection unreliable on short text
- Weak supervision in AFND

## How to Run Locally

1. Clone the repo
   git clone https://github.com/KhaledTTarabay/Project-Mizan.git
   cd Project-Mizan

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux

3. Install dependencies
   pip install -r requirements.txt

4. Download datasets
   - AFND: https://www.kaggle.com/datasets/murtadhayaseen/arabic-fake-news-dataset-afnd
   - ISOT: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset
   Place them in data/raw/

5. Process the data
   python data/processed/process_afnd.py
   python data/processed/process_isot.py
   python data/processed/merge.py

6. Train the models
   python model/train.py

7. Run the app
   streamlit run app.py