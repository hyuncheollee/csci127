#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 17, 2022
#This program will modify a map

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')
mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)
for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] > 6 and elevations[row,col] <= 20:
           floodMap[row,col,0] = 0.5
           floodMap[row,col,1] = 0.5
           floodMap[row,col,2] = 0.5
        elif elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,2] = 1.0  
        elif elevations[row,col] <= 6:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0] = 1.0
           floodMap[row,col,1] = 1.0
           floodMap[row,col,2] = 0.0
        else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%

plt.imsave('floodMap.png', floodMap)