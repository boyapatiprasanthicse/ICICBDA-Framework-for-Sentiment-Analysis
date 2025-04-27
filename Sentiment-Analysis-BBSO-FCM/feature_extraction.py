from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_features(text_corpus):
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(text_corpus)
    return X
