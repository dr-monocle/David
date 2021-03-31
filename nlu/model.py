import yaml
import json
import numpy as np
import os

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical

data = yaml.safe_load(open('nlu/train.yml', 'r').read())

# Reading the data

inputs, outputs = [], []

for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append('{}\{}'.format(command['entity'], command['action']))

# Creating a dataset

    # Choosing a level of tokenization: words, chars, BPEs
chars = set()
    # Read all chars in the dataset
for i in inputs + outputs:
    for ch in i:
        if ch not in chars:
            chars.add(ch)
    
    # Map each char to an index
char2idx = {}
idx2char = {}

for k, ch in enumerate(chars):
    char2idx[ch]
    idx2char[k]

    # Create input data
max_sent = max([len(x) for x in inputs])
    
    # Create arrays
input_data = np.zeros((len(inputs), max_sent, len(chars)), dtype='int32')

for i, input in enumerate(inputs):
    for k, ch in enumerate(input):
        input_data[i, k, char2idx[ch]]

output_data = np.eye()
# output_data = to_categorical(output_data, len(output_data))

print(output_data[0])

#print(input_data.shape)
# print(len(chars))
# print('Max input seq: ', max_sent)
