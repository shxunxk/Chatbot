import spacy
from Train.FindPatternResponse import train
from Functions.Speak import Speak
import json
from Train.FindPatternResponse import TrainPattern

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
    for token in res:
        tokens.append(token)
        lemmatized[token.text] = token.lemma_
        grammatics[token.text] = token.pos_
        dependency[token.text] = token.dep_
    for ent in res.ents:
        entity[ent.text] = ent.label_

    intent = train(sentence)
    for inten in intents["intents"]:
        if(inten["tag"] == intent):
            pattern = TrainPattern(sentence, inten['patterns'])
            response = TrainPattern(pattern, inten['responses'])
            Speak(response)