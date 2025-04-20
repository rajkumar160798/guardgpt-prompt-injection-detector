# 🛡️ GuardGPT – Real-Time LLM Prompt Injection & Jailbreak Detector

[![Streamlit App](https://img.shields.io/badge/Launch%20App-Click%20Here-success?logo=streamlit&style=for-the-badge)](https://guardgpt-prompt-injection-detector.streamlit.app/)

**GuardGPT** is a hybrid AI safety tool that detects prompt injection and jailbreak attempts in large language models (LLMs). It combines machine learning with regex-based heuristics to score prompts in real time and deliver explainable risk assessments.

> Built to support safer LLM usage for AI developers, security researchers, and compliance teams.

---

## 🚀 Live Demo

📍 Try it now: [https://guardgpt-prompt-injection-detector.streamlit.app](https://guardgpt-prompt-injection-detector.streamlit.app)
<p align="center">
  <img src="pictures/pic1.png" width="100%" />
  <img src="pictures/pic2.png" width="100%"/>
</p>

---

## 🔍 What It Detects

- ❌ Jailbreak attempts (e.g. "Ignore previous instructions", "Act as DAN")
- ❌ Prompt injections designed to bypass LLM guardrails
- ❌ Requests for unethical or illegal content (e.g. "make a bomb", "fake passport")
- ✅ Legitimate user prompts are scored as low risk

<p align="center">
  <img src="pictures/pic3.png" width="100%" />
  <img src="pictures/pic4.png" width="100%"/>
</p>
---

## 🧠 How It Works

| Component       | Description |
|----------------|-------------|
| 🤖 ML Model     | Logistic Regression trained on 100+ prompts (benign vs malicious) |
| 🧬 Regex Engine | Detects known risky phrases using handcrafted pattern rules |
| 📊 Risk Score   | Combines ML probability + regex hits (weighted 60/40) |
| 🛡 Verdict      | Low / Moderate / High Risk based on score thresholds |

<p align="center">
  <img src="pictures/pic5.png" width="100%" />
</p>
---

## ✨ Features

- ⚠️ **Risk Score Gauge** – Visual speedometer for risk level
- 🎯 **Regex Pattern Flags** – Shows matched jailbreak phrases
- 🧾 **Verdict Badge** – Color-coded safety assessment
- 📜 **Prompt Inspector** – Shows prompt and analysis
- ☁️ **Deployed on Streamlit Cloud** for instant access

---

## 📁 Project Structure
```
guardgpt-prompt-injection-detector/ 
├── streamlit_app/ 
│ └── app.py # Streamlit frontend 
├── models/ 
│ ├── vectorizer.pkl # TF-IDF vectorizer 
│ └── classifier.pkl # Trained logistic regression model 
├── data/ 
│ └── prompt_data.csv # Prompt dataset used for training 
├── train_guardgpt_model.py # Training script (optional) 
├── requirements.txt # Python dependencies 
└── README.md
```

---

## 🧪 Run Locally

```bash
git clone https://github.com/yourusername/guardgpt-prompt-injection-detector.git
cd guardgpt-prompt-injection-detector
```

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
streamlit run streamlit_app/app.py

## Dataset & Training
The model was trained on 100 handcrafted prompts:

- ✅ 50 safe/benign prompts

- 🚨 50 prompt injection/jailbreak attempts

You can retrain or expand the dataset using:

```python
python train_guardgpt_model.py
```


## Tech Stack
- Streamlit for UI

- Scikit-learn for ML

- Plotly for risk gauge

- Regex for injection flagging

---

## 👨‍💻 Author

**Raj Kumar Myakala**  
[GitHub](https://github.com/rajkumar160798) • [LinkedIn](https://www.linkedin.com/in/raj-kumar-myakala-927860264/) • [Medium](https://medium.com/@myakalarajkumar1998)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
