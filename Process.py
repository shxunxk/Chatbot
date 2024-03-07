import spacy
from Models.Load import load_and_predict
from Functions.Speak import Speak
import json
from Train.TrainPatterns import TrainPattern

with open('Data/intents.json') as f:
    intents = json.load(f)

nlp = spacy.load("en_core_web_sm")

def Process(sentence):
    doc = nlp(sentence)
    tokens= []
    lemmatized = {}
    grammatics = {}
    entity = {}
    dependency = {}
    res = nlp(doc)
    for idx,token in enumerate(res):
        tokens.append(token)
        lemmatized[token.text] = token.lemma_
        tokens[idx] = lemmatized[token.text]
        grammatics[token.text] = token.pos_
        dependency[token.text] = token.dep_

    for ent in res.ents:
        entity[ent.text] = ent.label_

    print(lemmatized, grammatics)

    intent = load_and_predict(sentence)
    for inten in intents["intents"]:
        if(inten["tag"] == intent):
            pattern = TrainPattern(sentence, inten['patterns'])
            response = TrainPattern(pattern, inten['responses'])
            Speak(response)