import pickle
from sklearn.utils.validation import check_is_fitted

with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("models/classifier.pkl", "rb") as f:
    clf = pickle.load(f)

# Check if vectorizer is fitted
check_is_fitted(vectorizer, attributes=["idf_"])
print("Vectorizer and classifier loaded successfully!")