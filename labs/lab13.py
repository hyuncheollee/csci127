#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 29, 2022
#This program will print 3 brown turtles that make a triangle

import turtle
pearl = turtle.Turtle()
wm = turtle.Screen()
turtle.colormode(255)
pearl.shape("turtle")
pearl.pencolor(150,75,0)
pearl.color(150,75,0)

for i in range(3):
    pearl.forward(100)
    pearl.left(120)
    pearl.stamp()


wm.exitonclick()
