import os
import pathlib
import statistics as stats

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).readlines()

delims = {'(':')',')':'(','[':']',']':'[','{':'}','}':'{','<':'>','>':'<'}
startChars = ['(','[','{','<']
errors = {')':0,']':0,'}':0,'>':0}
completes = {')':0,']':0,'}':0,'>':0}
completePoints = {')': 1,']': 2,'}': 3,'>': 4}
completionScores = []

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
    else:
        score = 0
        for x in reversed(pairs):
            score = (score * 5) + completePoints[delims[x[0]]]
        completionScores.append(score)

print(f"Solution: {stats.median(completionScores)}")