import yaml

# roman fix
with open("data/vocab.ro.yml", encoding="utf8") as f:
    rdata = yaml.load(f, Loader=yaml.SafeLoader)

for i, key in enumerate(rdata):
    rdata[key] = i

with open("vocab.clean.ro.yml", "w", encoding="utf8") as f:
    yaml.dump(rdata, f)

# Urdu fix
with open("data/vocab.ur.yml", encoding="utf8") as f:
    udata = yaml.load(f, Loader=yaml.SafeLoader)

for i, key in enumerate(udata):
    udata[key] = i

with open("vocab.clean.ur.yml", "w") as f:
    yaml.dump(udata, f, allow_unicode=True)
