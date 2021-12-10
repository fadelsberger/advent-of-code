import os
import pathlib

dir = pathlib.Path(__file__).parent.absolute()
inputData = open(os.path.join(dir, "input.txt")).readlines()