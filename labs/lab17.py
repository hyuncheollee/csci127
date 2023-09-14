#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 17, 2022
#This program asks users for output file name to save the following image

import matplotlib.pyplot as mpl
import numpy as np

name = input("Enter output file name: ")
empty = np.zeros([30,30,3])

for row in range(30):
    for col in range(30):
        if (row > 4) and (row < 9) and (col > 4) and (col < 26):
            empty[row, col, 2] = 1
        elif (row > 7) and (row < 26) and (col > 12) and (col < 17):
            empty[row, col, 1] = 1
        else: 
            empty[row, col, 0] = 1
            empty[row, col, 1] = 1

mpl.imsave(name + ".png", empty)