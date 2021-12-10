import os
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).readlines()
horizontal = 0
depth = 0

for inputLine in inputData:
    #if not inputLine.strip():
    line = inputLine.split()
    direction = line[0]
    units = line[1]
    if direction == "forward":
        horizontal += int(units)
    if direction == "up":
        depth -= int(units)
    if direction == "down":
        depth += int(units)

result = horizontal * depth

print(f"Horizontal: {horizontal}")
print(f"Depth: {depth}")
print(f"Result: {result}")