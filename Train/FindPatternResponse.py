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
    # Sample data
    data = {
        "text": ["hello", "How are you?", "Tell me a joke", "What's the weather like today?", "Set a timer for 10 minutes", "Fuck you"],
        "label": ["greeting", "health", "humor", "weather", "timer", "swear"]
    }

    # Load data into DataFrame
    df = pd.DataFrame(data)

    # Preprocess text data
    sentences = [text.split() for text in df["text"]]
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            sentences[i][j] = sentences[i][j].lower()

    # Train Word2Vec model
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

    # Encode labels
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(df["label"])

    # Convert words to vectors and pad sequences
    X = []
    max_len = 0
    for text in sentences:
        seq = [model.wv[word] for word in text if word in model.wv]
        X.append(seq)
        max_len = max(max_len, len(seq))
    
    # Pad sequences to the maximum length
    X = pad_sequences(X, maxlen=max_len, padding='post', dtype='float32')

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    # Define the model architecture
    # Define the model architecture
    model = Sequential()
    model.add(LSTM(units=128, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
    model.add(LSTM(units=64))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=len(label_encoder.classes_), activation='softmax'))


    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    # Save the model
    current_directory = os.getcwd()
    os.makedirs(f"{current_directory}/Models", exist_ok=True)
    model_path = f"{current_directory}/Models/Patternmodel.h5"
    model.save(model_path)

    print(f"Model saved at {model_path}")

if __name__ == "__main__":
    train()
