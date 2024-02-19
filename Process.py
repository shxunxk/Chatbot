import spacy

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
    print(dependency, entity)