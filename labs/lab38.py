#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 5, 2022
#This program will draw pentagons inside pentagons

import math
import turtle
pearl = turtle.Turtle()

def drawPantegon(pearl, length, numEdges):
    if numEdges > 0:
        pearl.forward(length)
        pearl.left(72)
        drawPantegon(pearl, length, numEdges - 1)
        
def cornerPantegon(t, length):
    if length >= 25:
        drawPantegon(t, length, 5)
        half = length // 2
        cornerPantegon(t, half)    

def nestedPantegon(pearl, length):
    if length >= 25:
        drawPantegon(pearl, length, 5)
        pearl.forward(length / 2)
        pearl.left(36)
        update = length * math.sin(54 / 180 * math.pi)
        nestedPantegon(pearl, update)