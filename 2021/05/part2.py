import os
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.absolute()
inputData = open(os.path.join(dir, "input.txt")).readlines()

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
    a = line[0]
    b = line[1]
    c = line[2]
    d = line[3]
    if line[0] == line[2]:
        for i in range(min(line[1],line[3]),max(line[1],line[3])+1):
            coordTable[i,line[0]] += 1
    elif line[1] == line[3]:
        for i in range(min(line[0],line[2]),max(line[0],line[2])+1):
            # print(f"i: {i}")
            coordTable[line[1],i] += 1
    elif line[0] < line[2]:
        if line[1] < line[3]:
            while a <= c and b <= d:
                coordTable[b,a] += 1
                a += 1
                b += 1
        if line[1] > line[3]:
            while a <= c and b >= d:
                coordTable[b,a] += 1
                a += 1
                b -= 1
    elif line[0] > line[2]:
        if line[1] < line[3]:
            while a >= c and b <= d:
                coordTable[b,a] += 1
                a -= 1
                b += 1
        if line[1] > line[3]:
            while a >= c and b >= d:
                coordTable[b,a] += 1
                a -= 1
                b -= 1
    
        
result = (coordTable>=2).sum()
print(f"result: {result}")
