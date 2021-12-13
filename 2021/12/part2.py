import os
import pathlib

# checking if possible to visit
def canVisit(curr: str, path: list) -> bool:
    if curr.islower():
        if path.count(curr) == 0:
            return True
        else:
            if any(cave.islower() for cave in paths):
                lowers = [x for x in paths if x.islower()]
                multis = [x for x in [y for y in paths if y.islower()] if path.count(x) > 1]
                if len(multis) > 0:
                    return False
                for i in lowers:
                    if path.count(i) == 1 and i == curr and len(multis) == 0:
                        visit = True
                    if path.count(i) > 2:
                        visit = False
                        break
                    else:
                        visit = True
                return visit
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
    if line[0] == "start":
        first = "START"
        second = line[1]
    elif line[1] == "start":
        first = "START"
        second = line[0]
    elif line[0] == "end":
        second = "END"
        first = line[1]
    elif line[1] == "end":
        first = line[0]
        second = "END"
    else:
        first = line[0]
        second = line[1]

    if first in paths:
        paths[first].append(second)
    else:
        paths[first] = [second]
    if first != "START" and second != "END":
        if second in paths:
            paths[second].append(first)
        else:
            paths[second] = [first]

allPaths = nodeSearch(paths,"START","END")
print(f"{len(allPaths)}")