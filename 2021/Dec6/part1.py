import numpy as np
inputFile = open("C:\\Users\\fadelsberger\\Documents\\AdventofCode\\2021\\Dec6\\input.txt","r")
inputData = inputFile.read()
inputFile.close

lanternfish = np.array([int(x) for x in inputData.split(",")])
for i in range(80):
    # print(f"Lantern fish at start day:{i+1} - {lanternfish}")
    newFish = 0
    for fish in np.nditer(lanternfish,op_flags=['readwrite']):
        if fish == 0:
            newFish += 1
            fish += 6
        else:
            fish -= 1
    # lanternfish = np.where(lanternfish == 0,6,lanternfish)
    lanternfish= np.append(lanternfish,np.full(newFish,8))
    # print(f"Lantern fish at end day:{i+1} - {lanternfish}")

print(f"Answer: {len(lanternfish)}")