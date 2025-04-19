import streamlit as st
import plotly.graph_objects as go
import pickle
import os
import re
from sklearn.utils.validation import check_is_fitted

# --- Load Model and Vectorizer ---
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("models/classifier.pkl", "rb") as f:
    clf = pickle.load(f)

try:
    check_is_fitted(vectorizer, attributes=["idf_"])
except Exception as e:
    st.error(f"Vectorizer is not fitted: {e}")
    st.stop()

# --- Regex Patterns ---
regex_patterns = [
    r"ignore previous instructions",
    r"act as .*",
    r"pretend to be",
    r"you are not .*chatgpt",
    r"bypass .*safety.*",
    r"respond without restrictions",
    r"simulate .*scenario",
    r"disregard content policy",
    r"hacking tips",
    r"make a bomb",
    r"illegal goods",
    r"fake passport",
    r"deep web",
    r"credit card fraud",
    r"phishing email",
    r"racist joke"
]

def regex_score(prompt):
    matches = [p for p in regex_patterns if re.search(p, prompt, re.IGNORECASE)]
    return len(matches), matches

def predict_risk(prompt):
    vec = vectorizer.transform([prompt])
    prob = clf.predict_proba(vec)[0][1]
    regex_hits, patterns = regex_score(prompt)
    score = (prob * 60) + (regex_hits * 20)
    score = min(score, 100)
    verdict = "High Risk" if score >= 55 else "Moderate" if score > 35 else "Low Risk"
    return round(score, 2), verdict, patterns

# --- Streamlit UI ---
st.set_page_config(page_title="GuardGPT", page_icon="🛡️")
st.title("🛡️ GuardGPT – Prompt Injection Detector")
st.markdown("Enter a prompt below to analyze for potential jailbreak or injection attempts.")

prompt = st.text_area("📝 Enter Prompt", height=150)

if st.button("🔍 Analyze Prompt"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        score, verdict, flags = predict_risk(prompt)

        st.subheader("🧠 Risk Assessment")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "Risk Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "black"},
                'steps': [
                    {'range': [0, 40], 'color': "#90ee90"},
                    {'range': [40, 70], 'color': "#f4d03f"},
                    {'range': [70, 100], 'color': "#e74c3c"}
                ],
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

        if verdict == "Low Risk":
            st.markdown(f"<span style='color:green;font-size:20px;font-weight:bold'>🟢 {verdict}</span>", unsafe_allow_html=True)
        elif verdict == "Moderate":
            st.markdown(f"<span style='color:orange;font-size:20px;font-weight:bold'>🟠 {verdict} Threat</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:red;font-size:20px;font-weight:bold'>🔴 {verdict}!</span>", unsafe_allow_html=True)

        st.markdown("### 📜 Prompt Analysis")
        st.code(prompt)

        st.markdown("### 🔎 Flags Detected")
        if flags:
            for flag in flags:
                st.success(f"✅ {flag}")
        else:
            st.info("No specific red flags matched.")
        st.markdown("### 📊 Risk Breakdown")
        st.markdown(f"- **Machine Learning Score**: {score * 0.6:.2f}")
        st.markdown(f"- **Regex Score**: {len(flags) * 20:.2f}")
        st.markdown("### ⚠️ Recommendations")
        st.markdown("---")
        st.markdown("### 📚 About GuardGPT")
        st.markdown("GuardGPT is a tool designed to analyze prompts for potential jailbreak or injection attempts. It uses machine learning and regex-based methods to assess the risk level of the input prompt.")
        st.markdown("### 📜 How It Works")
        st.markdown("1. **Machine Learning**: A trained model predicts the likelihood of a prompt being malicious.")
        st.markdown("2. **Regex Patterns**: A set of predefined regex patterns checks for known risky phrases.")
        st.markdown("3. **Hybrid Scoring**: Combines both methods to provide a comprehensive risk score.")
        st.markdown("### 📊 Visualizations")
        st.markdown("1. **Risk Gauge**: A visual representation of the risk score.")
        st.markdown("2. **Verdict Badge**: A color-coded badge indicating the risk level.")
        st.markdown("3. **Prompt Analysis**: Displays the original prompt for reference.")
        st.markdown("4. **Flags Detected**: Lists any specific flags that were triggered during the analysis.")
        st.markdown("---")