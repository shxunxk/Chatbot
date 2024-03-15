import os
import pandas as pd
import joblib

def load_and_predict(sentence):
    model_path = f"{os.getcwd()}/Models/Patternmodel.joblib"
    
    loaded_model = joblib.load(model_path)

    predictions = loaded_model.predict(pd.Series(sentence))
    
    return predictions[0]

# a = load_and_predict('Hello')
# print(a)