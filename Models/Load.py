import os
import pandas as pd
import numpy as np
import joblib

def load_and_predict(sentence):
    print(sentence)
    model_path = f"{os.getcwd()}/Models/Patternmodel.joblib"
    loaded_object = joblib.load(model_path)

    if isinstance(loaded_object, tuple) and len(loaded_object) == 2:
        model, clf = loaded_object

        tokens = sentence.split()
        sentence_vec = np.mean([model.wv[word] for word in tokens if word in model.wv] or [np.zeros(100)], axis=0)
        print(sentence_vec)
        if np.all(sentence_vec == 0):
            return "unknown"

        prediction = clf.predict([sentence_vec])

        return prediction[0]

    else:
        print("Error: Unexpected format of loaded model file.")
        return None

# a = load_and_predict('Hello')
# print(a)