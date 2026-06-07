import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

phishing_keywords = [
    "winner",
    "lottery",
    "urgent",
    "verify",
    "bank",
    "password",
    "reward",
    "claim",
    "free",
    "click"
]


# =====================================
# LOAD DATASET
# =====================================

data = pd.read_csv("emails.csv")

# Display dataset info

print("Dataset Loaded Successfully")
print("\nColumns:")
print(data.columns)

print("\nTotal Rows:", len(data))

# =====================================
# DETECT COLUMN NAMES
# =====================================

label_column = data.columns[0]
message_column = data.columns[1]

# =====================================
# CONVERT LABELS
# =====================================

data[label_column] = data[label_column].map({
    "ham": 0,
    "spam": 1
})

# =====================================
# FEATURES AND LABELS
# =====================================

X = data[message_column]
y = data[label_column]

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================
# TF-IDF FEATURE EXTRACTION
# =====================================

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# =====================================
# TRAIN MODEL
# =====================================

model = MultinomialNB()

model.fit(X_train, y_train)

# =====================================
# PREDICTION
# =====================================

predictions = model.predict(X_test)

# =====================================
# ACCURACY
# =====================================

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    "\nModel Accuracy:",
    round(accuracy * 100, 2),
    "%"
)
print(
    "\nDataset Split:"
)
print(
    f"Training Samples: {len(X_train.toarray())}"
)
print(
    f"Testing Samples: {len(X_test.toarray())}"
)
# =====================================
# CONFUSION MATRIX
# =====================================

cm = confusion_matrix(
    y_test,
    predictions
)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Safe", "Phishing"]
)

display.plot()

plt.title("Phishing Detection Confusion Matrix")

plt.savefig("confusion_matrix.png")

plt.show()

print(
    "\nConfusion Matrix Saved As confusion_matrix.png"
)

# =====================================
# USER TESTING
# =====================================

while True:

    print("\n--------------------------------")

    email = input(
        "\nEnter Email Text (type exit to quit): "
    )

    if email.lower() == "exit":
        break

    # ==========================
    # Keyword Detection
    # ==========================

    keyword_hits = []

    for word in phishing_keywords:

        if word in email.lower():
            keyword_hits.append(word)

    # ==========================
    # URL Detection
    # ==========================

    urls = re.findall(
        r'https?://\S+|www\.\S+',
        email
    )

    # ==========================
    # ML Prediction
    # ==========================

    email_vector = vectorizer.transform(
        [email]
    )

    result = model.predict(
        email_vector
    )[0]

    probability = model.predict_proba(
        email_vector
    )[0]

    confidence = max(probability) * 100

    if result == 1:

        print("\nPrediction: PHISHING")

    else:

        print("\nPrediction: SAFE")

    print(
        f"Confidence: {confidence:.2f}%"
    )

    # ==========================
    # Risk Score
    # ==========================

    risk_score = 0

    risk_score += len(keyword_hits)

    risk_score += len(urls) * 2

    # ==========================
    # Display Findings
    # ==========================

    if keyword_hits:

        print("\nSuspicious Keywords Found:")

        for word in keyword_hits:
            print("-", word)

    if urls:

        print("\nURLs Detected:")

        for url in urls:
            print("-", url)

    if risk_score >= 3:

        print(
            "\nWARNING: Suspicious phishing indicators detected."
        )