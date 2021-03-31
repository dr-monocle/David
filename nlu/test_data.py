import yaml

with open('train.yml').read() as f:

    data = yaml.safe_load(f)

print(data)