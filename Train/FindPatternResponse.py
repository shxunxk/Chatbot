import os
import pandas as pd
import numpy as np
import joblib
from gensim.models import Word2Vec
from sklearn.svm import SVC

def train():
    data = {
        "text": ["hello", "How are you?", "Tell me a joke", "What's the weather like today?", "Set a timer for 10 minutes", "Fuck you"],
        "label": ["greeting", "health", "humor", "weather", "timer", "swear"]
    }

    df = pd.DataFrame(data)

    sentences = [text.split() for text in df["text"]]

    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            sentences[i][j] = sentences[i][j].lower()
    print(sentences)

    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

    X = np.array([np.mean([model.wv[word] for word in text.split() if word in model.wv] or [np.zeros(100)], axis=0) for text in df["text"]])
    print(X)
    clf = SVC()
    clf.fit(X, df["label"])

    current_directory = os.getcwd()
    os.makedirs(f"{current_directory}/Models", exist_ok=True)
    model_path = f"{current_directory}/Models/Patternmodel.joblib"
    joblib.dump((model, clf), model_path)

    print(f"Models saved at {model_path}")

train()
