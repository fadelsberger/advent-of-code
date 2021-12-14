import os
import pathlib

dir = pathlib.Path(__file__).parent.absolute()
inputData = open(os.path.join(dir, "input.txt")).read()

rules = {}
input = inputData.split('\n\n')
template = [x for x in input[0]]
rawRules = input[1].splitlines()
for rule in rawRules:
    key, result = rule.split(' -> ')
    rules[key] = result

counts = {}
for x in range(len(template)):
    if x + 1 < len(template):
        if template[x]+template[x+1] in counts:
            counts[template[x]+template[x+1]] += 1
        else:
            counts[template[x]+template[x+1]] = 1

charCount = {}
for ch in template:
    if ch in charCount:
        charCount[ch] += 1
    else:
        charCount[ch] = 1
for i in range(40):
    keyLoop = counts.copy()
    for key,value in keyLoop.items():
        if value > 0:
            for rule,result in rules.items():
                if key in rule:
                    if result in charCount:
                        charCount[result] += value
                    else:
                        charCount[result] = value
                    if key[0] + result in counts:
                        counts[key[0] + result] += value
                    else:
                        counts[key[0] + result] = value
                    if result + key[1] in counts:
                        counts[result + key[1]] += value
                    else:
                        counts[result + key[1]] = value
                    counts[key] -= value

for key,value in charCount.items():
    print(f'Count of {key}: {value}')
print(f'Solution: Max of {max(charCount.values())} - Min of {min(charCount.values())} = {max(charCount.values()) - min(charCount.values())}')