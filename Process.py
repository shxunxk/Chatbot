import spacy
from Models.Load import load_and_predict
from Functions.Speak import Speak
import json
from Train.TrainPatterns import TrainPattern
import Levenshtein

with open('Data/intents.json') as f:
    intents = json.load(f)

nlp = spacy.load("en_core_web_sm")

def similar_tag(intent, intents_data = intents):
    max_similarity = 0
    index = 0
    for idx,intent_data in enumerate(intents_data["intents"]):
        similarity = Levenshtein.ratio(intent, intent_data["tag"])
        if similarity > max_similarity:
            max_similarity = similarity
            index = idx
    return index

def Process(sentence):
    doc = nlp(sentence)
    tokens = [token.text for token in doc]
    tokens = [token.lower() for token in tokens]
    sentence = ' '.join(tokens)
    print(tokens)
    # lemmatized = {}
    # grammatics = {}
    # entity = {}
    # dependency = {}
    # res = nlp(doc)
    # for idx,token in enumerate(res):
    #     tokens.append(token)
    #     lemmatized[token.text] = token.lemma_
    #     tokens[idx] = lemmatized[token.text]
    #     grammatics[token.text] = token.pos_
    #     dependency[token.text] = token.dep_

    # for ent in res.ents:
    #     entity[ent.text] = ent.label_

    # print(lemmatized, grammatics)

    intent = load_and_predict(sentence)
    idx = similar_tag(intent)
    pattern = TrainPattern(sentence, intents['intents'][idx]['patterns'])
    response = TrainPattern(pattern, intents['intents'][idx]['responses'])
    Speak(response)
    
# Process('Hello')