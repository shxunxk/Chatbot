import numpy as np
import spacy
from sklearn.feature_extraction.text import CountVectorizer

nlp = spacy.load("en_core_web_sm")

string = 'Dr. Strange loves Pav Bhaji of Mumbai. Hulk loves Strange chaat of Delhi'

def stemming(word):
    return (word.lemma_)

def tokenize(text):
    sen = nlp(text)
    sentence = []
    for sent in sen.sents:
        for token in sent:
            sentence.append(stemming(token))
    return(sentence)

coll = tokenize(string)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform([string])
print(vectorizer.get_feature_names_out())
print(vectorizer.vocabulary_)
bag_of_words_array = X.toarray()
bag_of_words_dict = dict(zip(vectorizer.get_feature_names_out(), bag_of_words_array[0]))

print(X)
print(bag_of_words_dict)