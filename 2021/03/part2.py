import os
import pathlib

def listCalc(lst, rating, pos):
    count0 = 0
    count1 = 0
    for ele in lst:
        if ele[pos] == str(0):
            count0 += 1
        else:
            count1 += 1
    if rating == "oxy":
        if count1 >= count0:  
            return 1
        else:
            return 0
    elif rating == "co2":
        if count1 < count0:  
            return 1
        else:
            return 0

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).readlines()
listOfLists = []
charCount = 0
for inputLine in inputData:
    newL = list(inputLine.strip())
    charCount = len(newL)
    listOfLists.append(newL)

oxygen = listOfLists
co2 = listOfLists

for y in range(0, charCount):
    compVal = listCalc(oxygen, "oxy", y)
    oxygen = [x for x in oxygen if x[y] == str(compVal)]
    # print(f"oxygen at {y}: {oxygen}")
    if len(oxygen) == 1:
        break

for z in range(0, charCount):
    compVal = listCalc(co2, "co2", z)
    co2 = [x for x in co2 if x[z] == str(compVal)]
    # print(f"co2 at {z}: {co2}")
    if len(co2) == 1:
        break

print(f"Oxygen: {oxygen}")
print(f"c02: {co2}")
result = int(''.join(oxygen[0]),2) * int(''.join(co2[0]),2)
print(f"Result: {result}")