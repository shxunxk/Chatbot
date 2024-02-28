from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def TrainPattern(sample, set):

    # Vectorize the set using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(set + [sample])

    # Calculate cosine similarity
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    # Find the most similar text
    most_similar_index = similarities.argmax()
    most_similar_text = set[most_similar_index]

    return (most_similar_text)