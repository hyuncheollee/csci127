#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 17, 2022
#This program will modify a map

import matplotlib.pyplot as mpl
import numpy as np

name = input("Enter file name: ")
threshold = input("Enter threshold: ")
image = mpl.imread(name)
countSnow = 0
everythingElse = 0
threshold = float(threshold)

for row in range(image.shape[0]):
    for col in range(image.shape[1]):
        if (image[row, col, 0] > threshold) and (image[row, col, 1] > threshold) and (image[row, col, 2] > threshold):
            countSnow += 1
        else:
            everythingElse += 1


percentage = countSnow / everythingElse
percentage *= 100
percentage = round(percentage, 2)

print("number of white pixels:", countSnow)
print("percent of white pixels:", percentage + "%")