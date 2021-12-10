import os
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).readlines()
yMax = len(inputData)
xMax = len(inputData[0].strip())
heightMap = np.empty((yMax, xMax), int)
for idx,data in enumerate(inputData):
    digits = [int(x) for x in data.strip()]
    heightMap[idx] = digits

sumLowpoints = 0

for y in range(yMax):
    for x in range(xMax):
        top = False
        bottom = False
        left = False 
        right = False
        # Top
        if y > 0:
            if heightMap[y,x] < heightMap[y-1,x]:
                top = True
        else:
            top = True
        # Right
        if (x+1) < xMax:
            if heightMap[y,x] < heightMap[y,x+1]:
                right = True
        else:
            right = True
        # Bottom
        if (y+1) < yMax:
            if heightMap[y,x] < heightMap[y+1,x]:
                bottom = True
        else:
            bottom = True
        # Left
        if x > 0:
            if heightMap[y,x] < heightMap[y,x-1]:
                left = True
        else:
            left = True
        if top and bottom and left and right:
            sumLowpoints += (heightMap[y,x]+1)
print(f"{sumLowpoints}")