import yaml
import json
import numpy as np

data = yaml.safe_load(open('nlu/train.yml', 'r').read())

# Reading the data

inputs, outputs = [], []

for command in data['commands']:
    inputs.append(command['input'])
    outputs.append('{}\{}'.format(command['entity'], command['action']))

# Creating a dataset

    # Choosing a level of tokenization: words, chars, BPEs
chars = set()
    # Read all chair in the dataset
for i in inputs + outputs:
    for ch in i:
        if ch not in chars:
            chars.add(ch)

    # Create an input data


print(len(chars))
