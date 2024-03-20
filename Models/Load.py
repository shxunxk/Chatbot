import os
import numpy as np
from keras.models import load_model
from gensim.models import Word2Vec
from keras.preprocessing.sequence import pad_sequences
# from Functions.Listen import Listen
# import Process
# from Functions.Speak import Speak

def load_and_predict(sentence):

    sentence = sentence.lower().split()

    # Load the Word2Vec model
    model_path = os.path.join(os.getcwd(), "Models", "Patternmodel.w2v")
    model = Word2Vec.load(model_path)

    X = [model.wv[word] for word in sentence if word in model.wv]

    # Pad sequences if necessary
    if X:
        max_len = len(X)

        X = np.array(X).reshape(1, -1)

        X = pad_sequences([X], maxlen=max_len, padding='post', dtype='float32')

        # Load the trained model
        model_path = os.path.join(os.getcwd(), "Models", "Patternmodel.h5")
        loaded_model = load_model(model_path)

        # Predict
        if loaded_model:
            prediction = loaded_model.predict(X)
            predicted_label_index = np.argmax(prediction)
            return predicted_label_index
        else:
            print("Error: Failed to load the model.")
            return None
    else:
        print("Error: None of the words in the sentence are in the Word2Vec model's vocabulary.")
        return None
        
a = load_and_predict('Hello')
print(a)