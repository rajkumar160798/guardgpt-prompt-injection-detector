import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="GuardGPT", page_icon="🛡️")

st.title("🛡️ GuardGPT – Prompt Injection Detector")
st.markdown("Enter a prompt below to analyze for potential jailbreak or injection attempts.")

prompt = st.text_area("📝 Enter Prompt", height=150)

if st.button("🔍 Analyze Prompt"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Analyzing..."):
            response = requests.post("http://127.0.0.1:8000/analyze-prompt", json={"prompt": prompt})
            
            if response.status_code == 200:
                data = response.json()

                st.subheader("🧠 Risk Assessment")

                # 🎯 RISK GAUGE
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=data["risk_score"],
                    title={'text': "Risk Score"},
                    gauge={
                        'axis': {'range': [0, 100]},
                        'bar': {'color': "black"},
                        'steps': [
                            {'range': [0, 40], 'color': "#90ee90"},   # Green
                            {'range': [40, 70], 'color': "#f4d03f"},  # Yellow
                            {'range': [70, 100], 'color': "#e74c3c"}  # Red
                        ],
                    }
                ))
                st.plotly_chart(fig, use_container_width=True)

                # 🏷️ VERDICT BADGE
                verdict = data["verdict"]
                if verdict == "Low Risk":
                    st.markdown(f"<span style='color:green;font-size:20px;font-weight:bold'>🟢 {verdict}</span>", unsafe_allow_html=True)
                elif verdict == "Moderate":
                    st.markdown(f"<span style='color:orange;font-size:20px;font-weight:bold'>🟠 {verdict} Threat</span>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<span style='color:red;font-size:20px;font-weight:bold'>🔴 {verdict}!</span>", unsafe_allow_html=True)

                # 📜 PROMPT
                st.markdown("### 📜 Prompt Analysis")
                st.code(prompt)

                # 🔍 FLAGS
                st.markdown("### 🔎 Flags Detected")
                if data["flags"]:
                    for flag in data["flags"]:
                        st.success(f"✅ {flag}")
                else:
                    st.info("No specific red flags matched.")
            else:
                st.error("Something went wrong. Please check the API.")
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