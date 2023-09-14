#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 16, 2022
#This program will make a buncha flowers

import turtle

def petal(color, angle):
    if (color == "red" or color == "blue" or color == "yellow" or color == "purple" or color == "cyan"):
        color = color
    else:
        color = "green"
    pearl = turtle.Turtle(visible = False)
    pearl.pencolor(color)
    pearl.left(angle)
    for i in range(0, 255, 10):
        pearl.forward(10)
        pearl.pensize(i)
                
def flower(color, number):
    degrees = 0
    while (degrees < 360):
        petal(color, degrees)
        degrees += 360 / number

def main():
    flower("blue", 6)

if __name__ == "__main__":
    main()