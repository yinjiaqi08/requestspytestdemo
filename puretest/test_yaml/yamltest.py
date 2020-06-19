import yaml
f = open('yaml.yml', encoding='utf-8')
res = yaml.load(f)
f.close()
print(res)
