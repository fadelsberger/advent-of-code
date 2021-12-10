import os
import pathlib
import numpy as np
# Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    # print(f"Count of {x}: {count}")
    return count

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).readlines()

listOfLists = []
charCount = 0
for inputLine in inputData:
    newL = list(inputLine.strip())
    charCount = len(newL)
    listOfLists.append(newL)

gamma = ""
epsilon = ""

for x in range(0, charCount):
    newList = []
    for y in range(0,len(listOfLists)):
        newList.append(listOfLists[y][x])
    if countX(newList,str(1)) > countX(newList,str(0)):
        gamma += str(1)
        epsilon += str(0)
    else:
        gamma += str(0)
        epsilon += str(1)
print(f"Gamma: {gamma}")
print(f"Epsilon: {epsilon}")

gammaRate = int(gamma,2)
epsilonRate = int(epsilon,2)
print(f"GammaRate: {gammaRate}")
print(f"EpsilonRate: {epsilonRate}")

result = gammaRate * epsilonRate
print(f"Result: {result}")

# if countX(first,1) > countX(first,0):
#     gammaDigitOne = 1
#     epsilonDigitOne = 0
# else:
#     gammaDigitOne = 0
#     epsilonDigitOne = 1
# if countX(second,1) > countX(second,0):
#     gammaDigitTwo = 1
#     epsilonDigitTwo = 0
# else:
#     gammaDigitTwo = 0
#     epsilonDigitTwo = 1
# if countX(third,1) > countX(third,0):
#     gammaDigitThree = 1
#     epsilonDigitThree = 0
# else:
#     gammaDigitThree = 0
#     epsilonDigitThree = 1
# if countX(fourth,1) > countX(fourth,0):
#     gammaDigitFour = 1
#     epsilonDigitFour = 0
# else:
#     gammaDigitFour = 0
#     epsilonDigitFour = 1
# if countX(fifth,1) > countX(fifth,0):
#     gammaDigitFive = 1
#     epsilonDigitFive = 0
# else:
#     gammaDigitFive = 0
#     epsilonDigitFive = 1

# gammaBit = str(gammaDigitOne) + str(gammaDigitTwo) + str(gammaDigitThree) +str(gammaDigitFour) +str(gammaDigitFive)
# epsilonBit = str(epsilonDigitOne) + str(epsilonDigitTwo) + str(epsilonDigitThree) +str(epsilonDigitFour) +str(epsilonDigitFive)

# print(f"Gamma: {gammaBit}")
# print(f"Epsilon: {epsilonBit}")