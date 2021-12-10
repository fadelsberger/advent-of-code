import os
import pathlib

dir = pathlib.Path(__file__).parent.absolute()
inputData = open(os.path.join(dir, "input.txt")).readlines()

delims = {'(':')',')':'(','[':']',']':'[','{':'}','}':'{','<':'>','>':'<'}
startChars = ['(','[','{','<']
errors = {')':0,']':0,'}':0,'>':0}
errorPoints = {')': 3,']': 57,'}': 1197,'>': 25137}

for line in inputData:
    pairs = []
    chars = [x for x in line.strip()]
    pairs.append([chars[0],''])
    for ch in chars[1:]:
        found = False
        if ch in startChars:
            pairs.append([ch,''])
        else:
            if pairs[-1][0] == delims[ch]:
                del(pairs[-1])
            else:
                errors[ch] += 1
                break
print(f"{errors}")
result = 0
for k,v in errors.items():
    result += v * errorPoints[k]
print(f"{result}")
                    
                        



