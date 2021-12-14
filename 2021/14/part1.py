import os
import pathlib

dir = pathlib.Path(__file__).parent.absolute()
inputData = open(os.path.join(dir, "input.txt")).read()

rules = {}
input = inputData.split('\n\n')
template = [x for x in input[0]]
rawRules = input[1].splitlines()
print(f"{template}")
print(f"{rawRules}")
for rule in rawRules:
    key, result = rule.split(' -> ')
    rules[key] = result

for i in range(40):
    temp = []
    for j in range(len(template)):
        temp.append(template[j])
        if j + 1 < len(template):
            if template[j] + template[j+1] in rules:
                temp.append(rules[template[j]+template[j+1]])
    template = temp

deduped = []
for x in template:
    if x not in deduped:
        deduped.append(x)

counts = {}
for y in deduped:
    print(f'Count of {y}: {template.count(y)}')
    counts[y] = template.count(y)
print(f"Solutions: Max of {max(counts.values())} - {min(counts.values())} = {max(counts.values())-min(counts.values())}")

