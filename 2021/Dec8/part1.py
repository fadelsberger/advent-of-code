import os
import pathlib


dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).readlines()

inputs = []
outputs = []

for line in inputData:
    line = line.split('|')
    inputs.append(line[0].strip())
    outputs.append(line[1].strip())

count = 0
for line in outputs:
    segments = line.split()
    for segment in segments:
        if len(segment) == 2:
            count += 1
        elif len(segment) == 4:
            count += 1
        elif len(segment) == 3:
            count += 1
        elif len(segment) == 7:
            count += 1

print(f"Answer: {count}")
