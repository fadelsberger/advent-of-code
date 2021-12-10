import numpy as np
inputFile = open("C:\\Users\\fadelsberger\\Documents\\AdventofCode\\2021\\Dec6\\input.txt","r")
inputData = inputFile.read()
inputFile.close

lanternfish = np.array([np.longlong(x) for x in inputData.split(",")])
fishAtDay = np.empty(0, dtype=np.longlong)
for i in range(9):
    fishAtDay = np.append(fishAtDay, np.count_nonzero(lanternfish == i))
    
for i in range(256):
    newFish = fishAtDay[0]
    fishAtDay[0] = fishAtDay[1]
    fishAtDay[1] = fishAtDay[2]
    fishAtDay[2] = fishAtDay[3]
    fishAtDay[3] = fishAtDay[4]
    fishAtDay[4] = fishAtDay[5]
    fishAtDay[5] = fishAtDay[6]
    fishAtDay[6] = fishAtDay[7] + newFish
    fishAtDay[7] = fishAtDay[8]
    fishAtDay[8] = newFish
    
solution = np.sum(fishAtDay)
print(f"Answer: {solution}")