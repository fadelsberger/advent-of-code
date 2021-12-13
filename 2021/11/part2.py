import os
import pathlib
import numpy as np

def isValidCoord(coords: list, yMax: int, xMax: int) -> bool:
    if coords[0] > yMax or coords[0] < 0:
        return False
    elif coords[1] > xMax or coords[1] < 0:
        return False
    else:
        return True

def getNeighbors(grid: list,y: int, x: int) -> list:
    neighbors = []
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            if (y,x) != (y+i,x+j):
                if y+i >= 0 and y+i < len(grid):
                    if x+j >= 0 and x+j < len(grid[0]):
                        if grid[y+i][x+j] != 0:
                            neighbors.append([y+i,x+j])
    return neighbors

def flash(grid: list,flashed: list, y: int, x: int):
    toFlash = []
    flashed.append([y,x])
    grid[y][x] = 0
    neighbors = getNeighbors(grid, y, x)
    for yy,xx in neighbors:
        if grid[yy][xx] != 0:
            grid[yy][xx] += 1
        if grid[yy][xx] > 9:
            toFlash.append([yy,xx])
    for yyy, xxx in toFlash:
        if grid[yyy][xxx] != 0:
            flash(grid, flashed, yyy, xxx)
        
dir = pathlib.Path(__file__).parent.absolute()
inputData = open(os.path.join(dir, "input.txt")).readlines()

grid = []
for line in inputData:
    row = []
    line = [int(x) for x in line.strip()]
    for ch in line:
        row.append(ch)
    grid.append(row)
    
yMax = len(grid)
xMax = len(grid[0])
flashed = []
simulFlash = 0
for i in range(500):
    for y in range(yMax):
        for x in range(xMax):
            grid[y][x] += 1
    
    for y in range(yMax):
        for x in range(xMax):
            if grid[y][x] > 9:
                flash(grid, flashed, y, x)
    if sum(map(sum,grid)) == 0:
        if simulFlash == 0:
            simulFlash = i+1
print(f"First simultaneous flash: {simulFlash}")