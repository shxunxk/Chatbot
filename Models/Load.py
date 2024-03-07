import os
import pandas as pd
import joblib

def load_and_predict(sentence):
    model_path = f"{os.getcwd()}/Patternmodel.joblib"
    
    # Load the saved model
    loaded_model = joblib.load(model_path)

    # Make predictions with the loaded model
    predictions = loaded_model.predict(pd.Series(sentence))
    
    return predictions[0]