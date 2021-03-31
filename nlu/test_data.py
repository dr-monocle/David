import yaml
import json

data = yaml.safe_load(open('nlu/train.yml', 'r').read())

for command in data['commands']:
    print(command)