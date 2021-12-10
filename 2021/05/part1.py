import os
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).readlines()

# inputData = inputFile.read().splitlines()

newData = []
maxX = 0
maxY = 0
for line in inputData:
    newL = line.replace(" -> ",",")
    newL = [int(i) for i in newL.split(",")]
    if newL[0] > maxX:
        maxX = newL[0]
    if newL[1] > maxY:
        maxY = newL[1]
    if newL[2] > maxX:
        maxX = newL[2]
    if newL[3] > maxY:
        maxY = newL[3]
    newData.append(newL)

coordTable = np.zeros((maxY+1, maxX+1))

for line in newData:
    if line[0] == line[2]:
        for i in range(min(line[1],line[3]),max(line[1],line[3])+1):
            coordTable[i,line[0]] += 1
    if line[1] == line[3]:
        for i in range(min(line[0],line[2]),max(line[0],line[2])+1):
            # print(f"i: {i}")
            coordTable[line[1],i] += 1
        
result = (coordTable>=2).sum()
print(f"result: {result}")