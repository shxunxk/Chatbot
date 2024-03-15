# import numpy as np
# import pandas as pd
# import random
# import json
# import torch
# from Brain.Brain import NeuralNet
# from Brain.NeuralNetwork import bag_of_words, tokenize, stemming

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# with open('C:/Users/Shaunak/Documents/Barbara/Data/intents.json', 'r') as json_data:
#     intents = json.load(json_data)

# FILE = 'TrainData.pth'
# data = torch.load(FILE)

# input_size = data['input_size']
# hidden_size = data['hidden_size']
# output_size = data['output_size']
# all_words = data['all_words']
# tags = data['tags']
# model_state = data['model_state']

# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()

# #--

# Name = 'Barbara'
# from Functions.Listen import Listen
# from Functions.Speak import Speak
# def Main():
#     sentence = Listen()
#     if sentence == 'bye':
#         exit()
#     X = bag_of_words((pd.Series(sentence)).values)
#     print(X.shape)
#     X = torch.from_numpy(X).to(device)
#     X = X.float()
#     output = model(X)

#     _ , predicted = torch.max(output, dim=1)
#     tag = tags[predicted.item()]
#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]

#     if prob.item() > 0.75:
#         for intent in intents['intents']:
#             if tag == intent['tag']:
#                 reply = random.choice(intents['responses'])
#                 Speak(reply)
# Main()

import spacy
import numpy
import pandas
from Functions.Listen import Listen
from Process import Process

sentence = Listen()
Process(sentence)