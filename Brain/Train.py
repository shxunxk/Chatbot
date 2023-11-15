from typing import ClassVar
import numpy as np
import pandas as pd
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from NeuralNetwork import bag_of_words, tokenize, stemming
from sklearn.preprocessing import LabelEncoder
from Brain import NeuralNet

with open('C:/Users/Shaunak/Documents/Barbara/Data/intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

sentences = []
tag_sentences = []

x_tr = []
y_tr = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    final_pattern = []
    for pattern in intent['patterns']:
        w =  tokenize(pattern)
        sentences.append(pattern)
        tag_sentences.append(tag)
        final_pattern.append(w)
        all_words.extend(w)
        
    xy.append((final_pattern, tag))

sentences = pd.Series(sentences)

ignore_words = [',','?','-','.','/','*','+','=']

all_words = [stemming(word) for word in all_words if w not in ignore_words]
all_words = sorted(set(all_words))

tags = sorted(set(tags))

X = bag_of_words(sentences.values)

for i in range(0,len(X)):
    x_tr.append(X[i])
    y_tr.append(tag_sentences[i])

x_tr = np.array(x_tr)
y_tr = np.array(y_tr)

epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(x_tr[0])
hidden_size = 8
output_size = len(tags)

print('Training the model')

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_tr)
        self.x_data = x_tr
        label_encoder = LabelEncoder()
        y_tr_encoded = label_encoder.fit_transform(y_tr)
        self.y_data = torch.LongTensor(y_tr_encoded)
        
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples
    
dataset = ChatDataset()

train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device=device)

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(epochs):
    for (words, labels) in train_loader:
        words = words.to(device, dtype=torch.float32)
        labels = labels.to(device, dtype=torch.long)
        output = model(words)
        loss = criterion(output, labels.squeeze())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}')


print(f'Final Loss: {loss.item():.4f}')

data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": hidden_size,
    'output_size': output_size,
    "all_words": all_words,
    "tags": tags
}

FILE = 'TrainData.pth'
torch.save(data,FILE)

print(f'Training completed, file saved')