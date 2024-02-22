# from transformers import AutoTokenizer, AutoModelForTokenClassification, TokenClassificationPipeline

# tokenizer = AutoTokenizer.from_pretrained('qanastek/XLMRoberta-Alexa-Intents-NER-NLU')
# model = AutoModelForTokenClassification.from_pretrained('qanastek/XLMRoberta-Alexa-Intents-NER-NLU')
# predict = TokenClassificationPipeline(model=model, tokenizer=tokenizer)
# res = predict("réveille-moi à neuf heures du matin le vendredi")
# print(res)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def train(sentence):
    data = {
        "text": ["Hello", "How are you?", "Tell me a joke", "What's the weather like today?", "Set a timer for 10 minutes"],
        "label": ["greeting", "health", "humor", "weather", "timer"]
    }

    import pandas as pd
    df = pd.DataFrame(data)

    train_data, test_data, train_labels, test_labels = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

    model = make_pipeline(CountVectorizer(), MultinomialNB())

    model.fit(train_data, train_labels)

    predictions = model.predict(pd.Series(sentence))
    return(predictions[0])