from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

sentences = [
    "python programming language",
    "machine learning models",
    "data science analysis",
    "football match today",
    "cricket players practice"
]

vec = TfidfVectorizer()
data = vec.fit_transform(sentences)

k = KMeans(n_clusters=2)
clusters = k.fit_predict(data)

print("Cluster Results:\n")

for i in range(len(sentences)):
    s = sentences[i]
    c = clusters[i]
    print("Sentence:", s)
    print("Cluster:", c)
    print()
