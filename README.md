# Phishing-Email-Detection-Model
Detecting spam emails using machine learing and using its algorithms like Naive-Bayes to identify Spam mails.
# Phishing Email Detection Model

## Objective

This project uses Machine Learning to classify emails/messages as Phishing (Spam) or Safe (Ham).

## Features

* Trains on a phishing and legitimate email dataset
* Uses TF-IDF feature extraction
* Uses Multinomial Naive Bayes classification
* Detects suspicious phishing keywords
* Detects URLs in messages
* Displays model accuracy
* Generates a confusion matrix
* Allows real-time user testing

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

## Dataset

SMS Spam Collection Dataset (5574 messages)

## Model

* TF-IDF Vectorizer
* Multinomial Naive Bayes

## Performance

Model Accuracy: 96.8%

## How to Run

Install dependencies:

pip install pandas scikit-learn matplotlib

Run the project:

python phishing_detector.py

## Example

Input:
URGENT! Verify your bank account now.

Output:
Prediction: SAFE
Confidence: 59.64%

Suspicious Keywords Found:

* urgent
* verify
* bank

WARNING: Suspicious phishing indicators detected.
