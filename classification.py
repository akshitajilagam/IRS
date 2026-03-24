import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dataset
text_data = [
    "free ticket win",
    "good morning",
    "earn money online",
    "how are you",
    "claim your prize",
    "nice to meet you"
]

labels = [1,0,1,0,1,0]

data = pd.DataFrame({"msg":text_data,"target":labels})

print("Dataset Used:")
print(data)

# Convert text into numbers
vector = CountVectorizer()
X = vector.fit_transform(data["msg"])

y = data["target"]

# Train model
lr = LogisticRegression()
lr.fit(X,y)

# Prediction
test = ["win free ticket"]
test_vec = vector.transform(test)

prediction = lr.predict(test_vec)

print("\nTesting Message:",test[0])

if prediction[0]==1:
    print("Prediction: Spam Message")
else:
    print("Prediction: Normal Message")
