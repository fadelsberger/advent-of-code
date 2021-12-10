import os
import pathlib
import numpy as np

def findBasin(point: list, basin: list, heightMap, yMax : int, xMax : int) -> int:
    y= point[0]
    x = point[1]
    basin.append(point)
    # Top
    if y > 0:
        if (heightMap[y,x]+1) <= heightMap[y-1,x] and heightMap[y-1,x] != 9:
            top = True
            findBasin([y-1,x], basin, heightMap, yMax, xMax)
    # Right
    if (x+1) < xMax:
        if (heightMap[y,x]+1) <= heightMap[y,x+1] and heightMap[y,x+1] != 9:
            right = True
            findBasin([y,x+1], basin, heightMap, yMax, xMax)
    # Bottom
    if (y+1) < yMax:
        if (heightMap[y,x]+1) <= heightMap[y+1,x] and heightMap[y+1,x] != 9:
            bottom = True
            findBasin([y+1,x], basin, heightMap, yMax, xMax)
    # Left
    if x > 0:
        if (heightMap[y,x]+1) <= heightMap[y,x-1] and heightMap[y,x-1] != 9:
            left = True
            findBasin([y,x-1], basin, heightMap, yMax, xMax)
    return [y,x]


dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).readlines()
yMax = len(inputData)
xMax = len(inputData[0].strip())
heightMap = np.empty((yMax, xMax), int)
for idx,data in enumerate(inputData):
    digits = [int(x) for x in data.strip()]
    heightMap[idx] = digits

sumLowpoints = 0
lowPoints = []
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
            lowPoints.append([y,x])

basins = []
for point in lowPoints:
    basin = []
    findBasin(point, basin, heightMap, yMax, xMax)
    deDupedBasin = []
    [deDupedBasin.append(x) for x in basin if x not in deDupedBasin]
    basins.append(len(deDupedBasin))

basins.sort(reverse=True)
solution = np.prod(basins[:3])
print(f"Solution: {solution}")