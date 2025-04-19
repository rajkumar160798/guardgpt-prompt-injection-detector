import pickle
import os

# Load model and vectorizer
model_path = os.path.join("models", "classifier.pkl")
vectorizer_path = os.path.join("models", "vectorizer.pkl")

with open(model_path, "rb") as f:
    clf = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

def predict_prompt(prompt: str):
    vectorized = vectorizer.transform([prompt])
    prob = clf.predict_proba(vectorized)[0][1]  # probability of label 1 (malicious)
    return prob
