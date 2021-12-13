import os
import pathlib

# checking if possible to visit
def canVisit(curr: str, path: list) -> bool:
    if curr.islower():
        if curr in path:
            return False
        else:
            return True
    else:
        return True

def nodeSearch(paths, start, end) -> list:
    pathList = []
    queue = []
    path = []
    path.append(start)
    queue.append(path.copy())
    while queue:
        path = queue.pop()
        current = path[len(path)-1]
        if current == end:
            pathList.append(path)
        else:
            for i in range(len(paths[current])):
                if canVisit(paths[current][i], path):
                    newpath = path.copy()
                    newpath.append(paths[current][i])
                    queue.append(newpath)
    return pathList


dir = pathlib.Path(__file__).parent.absolute()
inputData = open(os.path.join(dir, "input.txt")).readlines()

paths = {}
for line in inputData:
    line = line.strip().split("-")
    if line[1] == "start":
        first = "start"
        second = line[0]        
    elif line[0] == "end":
        second = "end"
        first = line[1]
    else:
        first = line[0]
        second = line[1]


    if first in paths:
        paths[first].append(second)
    else:
        paths[first] = [second]
    if first != "start" and second != "end":
        if second in paths:
            paths[second].append(first)
        else:
            paths[second] = [first]

allPaths = nodeSearch(paths,"start","end")
print(f"{allPaths}")
print(f"{len(allPaths)}")