#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 3, 2022
#This program counts the occurrence of a letter in a string

import numpy as np
import matplotlib.pyplot as mpl

print("Enter 1 to get upper right corner")
print("Enter 2 to get middle portion")
choice = int(input("Your choice: "))

if (choice == 1):
    inputName = input("Enter input file name: ")
    image = mpl.imread(inputName)
    height = image.shape[0]
    width = image.shape[1]
    outputName = input("Enter output file name: ")
    image2 = image[:int(height / 2), int(width / 2):]
    mpl.imsave(outputName, image2)
    
elif (choice == 2):
    inputName = input("Enter input file name: ")
    image = mpl.imread(inputName)
    height = image.shape[0]
    width = image.shape[1]
    outputName = input("Enter output file name: ")
    image2 = image[int(height / 4) :int(height * 0.75), int(width / 4) :int(width * 0.75)]
    mpl.imsave(outputName, image2)
    
else:
    print("wrong choice")