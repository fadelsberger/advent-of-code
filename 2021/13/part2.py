import os
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.absolute()
inputData = open(os.path.join(dir, "input.txt")).read()

folds = []
points = []
splidData = inputData.split('\n\n')
pointsList = splidData[0].strip()
directions = splidData[1].strip().split('\n')

for point in pointsList.split('\n'):
    xy = point.split(',')
    x = int(xy[0])
    y = int(xy[1])
    points.append([x,y])

for direction in directions:
    fold = {}
    line = direction.split()
    axisValue = line[2].split('=')
    fold['axis'] = axisValue[0]
    fold['value'] = int(axisValue[1])
    folds.append(fold)

for fold in folds:
    for point in points:
        if fold['axis'] == 'y' and point[1] > fold['value']:
            point[1] = fold['value'] - abs(point[1]-fold['value'])
        if fold['axis'] == 'x' and point[0] > fold['value']:
            point[0] = fold['value'] - abs(point[0]-fold['value'])

deduped = {(i,j) for i,j in points}
xMax = 0
yMax = 0
for x,y in deduped:
    if x > xMax:
        xMax = x
    if y > yMax:
        yMax = y
newGrid = np.zeros((yMax+1,xMax+1),int)

for point in deduped:
    newGrid[point[1],point[0]] = 1
with open(os.path.join(dir, "output.txt"), 'w') as file:
    file.write(f"{newGrid}")