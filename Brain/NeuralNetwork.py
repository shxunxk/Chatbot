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
            sentence.append(token)
    return(sentence)

vectorizer = CountVectorizer()

def bag_of_words(string):
    X = vectorizer.fit_transform([string])
    print(vectorizer.get_feature_names_out())
    print(vectorizer.vocabulary_)
    bag_of_words_array = X.toarray()
    print(bag_of_words_array)