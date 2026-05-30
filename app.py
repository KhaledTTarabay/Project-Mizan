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
            st.divider()
            scale_col1, scale_col2, scale_col3 = st.columns(3)
            with scale_col1:
                st.error("FAKE")
            with scale_col2:
                st.warning("UNCERTAIN")
            with scale_col3:
                st.success("CREDIBLE")

            if results["label"] == "Fake":
                fill = results["confidence"] / 100
                st.progress(
                    1 - fill, text=f"Credibility Score: {100 - results['confidence']}%"
                )
            else:
                fill = results["confidence"] / 100
                st.progress(fill, text=f"Credibility Score: {results['confidence']}%")
with tab2:
    st.header("Live Headlines")

    if st.button("Fetch Headlines"):
        from scraper.headlines import get_headlines

        with st.spinner("Fetching headlines..."):
            headlines = get_headlines()

        for h in headlines:
            result = predict(h["title"])

            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**[{h['title']}]({h['language'].upper()})")
                st.caption(f"{h["source"]} . {h['language'].upper()}")
            with col2:
                if result["label"] == "Fake":
                    st.error(f"{result['certainty']} Fake\n{result["confidence"]}%")
                else:
                    st.success(
                        f"{result['certainty']} Credible\n{result['confidence']}%"
                    )
            st.divider()
