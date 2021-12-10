import os
import pathlib
import numpy as np

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt")).read()

positions = np.array([int(x) for x in inputData.split(",")])
calc = np.median(positions)
fuel = 0
for pos in np.nditer(positions, op_flags=['readonly']):
    fuel += abs(pos - calc)

print(f"Fuel used: {fuel}")