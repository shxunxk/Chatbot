# Importing necessary libraries
import os
import pandas as pd
import numpy as np
import joblib
from gensim.models import Word2Vec
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.sequence import pad_sequences

def train():

    current_directory = os.getcwd()
    os.makedirs(f"{current_directory}/Models", exist_ok=True)

    data = {
        "text": ["hello", "How are you?", "Tell me a joke", "What's the weather like today?", "Set a timer for 10 minutes", "Fuck you", "What is you name", "created you"],
        "label": ["greeting", "health", "humor", "weather", "timer", "swear", "self", "creators"]
    }

    df = pd.DataFrame(data)

    sentences = [text.split() for text in df["text"]]
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            sentences[i][j] = sentences[i][j].lower()

    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

    w2v_model_path = os.path.join(current_directory, "Models", "Patternmodel.w2v")
    model.save(w2v_model_path)

    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(df["label"])

    X = []
    max_len = 0
    for text in sentences:
        seq = [model.wv[word] for word in text if word in model.wv]
        X.append(seq)
        max_len = max(max_len, len(seq))
    
    X = pad_sequences(X, maxlen=max_len, padding='post', dtype='float32')
    print(X)

    model = Sequential()
    model.add(LSTM(units=128, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
    model.add(LSTM(units=64))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=len(label_encoder.classes_), activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(X, labels, epochs=10, batch_size=32,)

    model_path = f"{current_directory}/Models/Patternmodel.h5"
    model.save(model_path)

    print(f"Model saved at {model_path}")

if __name__ == "__main__":
    train()