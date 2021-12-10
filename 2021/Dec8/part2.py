import os
import pathlib

def containsAll(str, set):
    for c in set:
        if c not in str: return 0
    return 1

def removeDupeChars(stringToDedupe) -> str:
    deduped = ""
    for char in stringToDedupe:
        if char not in deduped:
            deduped = deduped + char
    return deduped

def getDiffOnNums(smallerString, biggerString) -> str:
    result = biggerString
    for ch in smallerString:
        result = result.replace(ch, '')
    return result

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).readlines()
sumResult = 0
for line in inputData:
    digitList = [""] * 10
    inputs = []
    outputs = []
    line = line.split('|')
    inputs.append(line[0].strip())
    outputs.append(line[1].strip())

    segmentDict = dict.fromkeys(['a','b','c','d','e','f','g'])

    for line in inputs:
        digits = line.split()
        # digits = [''.join(sorted(x)) for x in digits]
        digitList[1] = next(x for x in digits if len(x) == 2)
        digitList[4] = next(x for x in digits if len(x) == 4)
        digitList[7] = next(x for x in digits if len(x) == 3)
        digitList[8] = next(x for x in digits if len(x) == 7)
        segmentDict['a'] = getDiffOnNums(digitList[1],digitList[7])
        digits6 = [x for x in digits if len(x) == 6]
        for i in digits6:
            if containsAll(set(i),digitList[4]):
                digitList[9] = i
                break
        segmentDict['e'] = getDiffOnNums(digitList[9],digitList[8])
        segmentDict['g'] = getDiffOnNums(digitList[4]+segmentDict['a'],digitList[9])
        digitList[2] = [x for x in digits if len(x) == 5 and segmentDict['e'] in x][0]
        segmentDict['d'] = getDiffOnNums(digitList[1]+segmentDict['a']+segmentDict['e']+segmentDict['g'],digitList[2])
        digitList[0] = digitList[8].replace(segmentDict['d'],'')
        segmentDict['c'] = getDiffOnNums(segmentDict['a'] + segmentDict['d'] + segmentDict['e'] + segmentDict['g'],digitList[2])
        segmentDict['f'] = getDiffOnNums(segmentDict['c'],digitList[1])
        segmentDict['b'] = getDiffOnNums(segmentDict['c'] + segmentDict['d'] + segmentDict['f'],digitList[4])
        digitList[6] = digitList[8].replace(segmentDict['c'],'')
        digitList[5] = digitList[6].replace(segmentDict['e'],'')
        digitList[3] = segmentDict['a'] + segmentDict['c'] + segmentDict['d'] + segmentDict['f'] + segmentDict['g']

        digitList = [''.join(sorted(x)) for x in digitList]

    outputDigits = ""
    for line in outputs:
        segments = line.split()
        segments = [''.join(sorted(x)) for x in segments]
        for segment in segments:
            for idx, digits in enumerate(digitList):
                if digits == segment:
                    outputDigits = outputDigits + str(idx)
                    break
    sumResult += int(outputDigits)

print(f"Answer: {sumResult}")
