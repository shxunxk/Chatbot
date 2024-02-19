import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import dataset, dataloader
from NeuralNetwork import bag_of_words, tokenize, stemming
from Brain import NeuralNet

with open('C:/Users/Shaunak/Documents/Barbara/Data/intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

sentences = []

x_tr = []
y_tr = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    final_pattern = []
    for pattern in intent['patterns']:
        w =  tokenize(pattern)
        sentences.append(pattern)
        final_pattern.append(w)
        all_words.extend(w)
        
    xy.append((final_pattern, tag))

ignore_words = [',','?','-','.','/','*','+','=']

all_words = [stemming(word) for word in all_words if w not in ignore_words]
all_words = sorted(set(all_words))

tags = sorted(set(tags))
print(sentences)
bag_of_words(sentences)