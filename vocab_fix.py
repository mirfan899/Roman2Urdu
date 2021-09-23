import yaml

with open("data/vocab.ro.yml", encoding="utf8") as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

for i, key in enumerate(data):
    data[key] = i

with open('vocab.clean.yml', 'w', encoding="utf8") as f:
    yaml.dump(data, f)
