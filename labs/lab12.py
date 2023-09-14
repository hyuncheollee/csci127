#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 26, 2022
#This program will make a pink eye

import turtle

pearl = turtle.Turtle()
wn = turtle.Screen()
turtle.colormode(255)

pearl.forward(100)
pearl.right(180)
for i in range(0,255,10):
    pearl.forward(10)
    pearl.pensize(i)
    pearl.color(i,0,i)
for j in range(255,0,-10):
    pearl.pensize(j)
    pearl.color(j,0,j)
    pearl.forward(10)



wn.exitonclick()