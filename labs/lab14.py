#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 29, 2022
#This program will print 3 brown turtles that make a triangle


#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np


img1 = plt.imread('csBridge.png')   #Read in image from csBridge.png
plt.imshow(img1)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img1.copy()        #make a copy of our image
img2[:,:,0] = 0          #Set the red channel to 0

plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave('csBridge_wo_red.png', img2)  #Save the image we created to the file: reds.png
