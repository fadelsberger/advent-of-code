inputFile = open("C:\\Users\\fadelsberger\\Documents\\AdventofCode2021\\Day2\\input.txt","r")
horizontal = 0
depth = 0
aim = 0

inputData = inputFile.readlines()

for inputLine in inputData:
    #if not inputLine.strip():
    line = inputLine.split()
    direction = line[0]
    units = line[1]
    if direction == "forward":
        horizontal += int(units)
        depth += aim * int(units)
    if direction == "up":
        aim -= int(units)
    if direction == "down":
        aim += int(units)

result = horizontal * depth
inputFile.close()

print(f"Horizontal: {horizontal}")
print(f"Depth: {depth}")
print(f"Result: {result}")