import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Load data
df = pd.read_csv("data/prompt_data.csv")
X = df["prompt"]
y = df["label"]

# Vectorizer
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=3000)
X_vec = vectorizer.fit_transform(X)

# Train model
clf = LogisticRegression()
clf.fit(X_vec, y)

# Save models
with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("models/classifier.pkl", "wb") as f:
    pickle.dump(clf, f)

print("✅ Model and vectorizer saved to /models")
