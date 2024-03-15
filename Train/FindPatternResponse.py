from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# from ..Functions.Speak import Speak
# from Functions.Listen import Listen
# from Process import Process

def train():
    data = {
        "text": ["Hello", "How are you?", "Tell me a joke", "What's the weather like today?", "Set a timer for 10 minutes", "Fuck you"],
        "label": ["greeting", "health", "humor", "weather", "timer", "swear"]
    }

    import pandas as pd
    df = pd.DataFrame(data)

    model = make_pipeline(CountVectorizer(), MultinomialNB())

    model.fit(df["text"], df["label"])
 
    current_directory = os.getcwd()
    os.makedirs(f"{current_directory}/Models", exist_ok=True)
    print(f"{current_directory}/Models/Patternmodel.joblib")

    joblib.dump(model, f"{current_directory}/Models/Patternmodel.joblib")


train()