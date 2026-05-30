import streamlit as st
from model.predict import predict

st.set_page_config(page_title="Mizan ميزان", layout="wide")

st.title("Mizan ميزان")
st.caption("Multilingual Misinformation Detector")

tab1, tab2 = st.tabs(["Analyse", "Live Headlines"])

with tab1:
    st.header("Analyze a Claim")

    text_input = st.text_area("Paste a claim in Arabic or English", height=150)

    if st.button("Analyze"):
        if text_input.strip() == "":
            st.warning("Please enter a claim first.")
        else:
            results = predict(text_input)

            st.subheader(f"{results['certainty']} {results['label']}")
            st.metric(label="Confidence", value=f"{results['confidence']}%")
            st.caption(f"Detected language: {results["language"].upper()}")
with tab2:
    st.header("Live Headlines")
