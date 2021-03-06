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

    # Choosing a level of tokenization: byte-level -> static vocab, handles out out-vocabulary

    # Create input data
max_sent = max([len(bytes(x.encode('utf-8'))) for x in inputs])

# Create arrays one-hot encoding (no of examples, seq length, vocab_size)
# Create arrays sparse encoding (no of examples, seq length)
input_data = np.zeros((len(inputs), max_sent, 256), dtype='float32')

# print(input_data.shape)
# exit()

for i, inp in enumerate(inputs):
    for k, ch in enumerate(inp.encode('utf-8')):
        input_data[i, k, int(ch)] = 1.0

# output_data = to_categorical(output_data, len(output_data))

# print(input_data[0].shape)

# print(input_data.shape)
# print(len(chars))
# print('Max input seq: ', max_sent)

labels = set(outputs)

with open('nlu\\entities.txt', 'w', encoding='utf-8') as f:
    for label in labels:
        f.write(label + '\n')
    f.close()

labels = open('nlu\\entities.txt', 'r', encoding='utf-8').read().split('\n')

label2idx = dict()
idx2label = dict()

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label

output_data = list()

for output in outputs:
    output_data.append(label2idx[output])

output_data = to_categorical(output_data, len(labels))


model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(labels), activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy', metrics=['acc'])

model.fit(input_data, output_data, epochs=256, verbose=0)

model.save('nlu\\model.h5')

# Classify any given text into a category of NLU framework


"""def classify(text):
    # Create input array
    x = np.zeros((1, max_sent, 256), dtype='float32')

    # Fill the x array with data from input text
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    out = model.predict(x)
    idx = out.argmax()

    # print(f'Text: "{text}" is classified as "{idx2label[idx]}".')

    return idx2labe


if __name__ == '__main__':
    while True:
        text = input('Enter some text: ')
        classify(text)"""
