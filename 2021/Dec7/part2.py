import os
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).read()

positions = np.array([int(x) for x in inputData.split(",")])
calc = np.floor(np.mean(positions))
fuel = 0
for pos in np.nditer(positions, op_flags=['readonly']):
    temp = 0
    temp = abs(pos - calc)
    fuel += ((temp*(1 + temp))/2)

print(f"Fuel: {fuel}")