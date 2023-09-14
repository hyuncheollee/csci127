#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 17, 2022
#This program will make a bunch of green and blue stripes

import matplotlib.pyplot as mpl
import numpy as np

size = input("Enter the size: ")
name = input("Enter output file: ")
size = int(size)

image = np.zeros([size, size, 3])

for row in range(size):
    for col in range(size):
        if (col % 2 == 0):
            image[row, col, 2] = 1
        elif (col % 2 == 1):
            image[row, col, 1] = 1

mpl.imsave(name + ".png", image)