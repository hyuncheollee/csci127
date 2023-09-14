#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 26, 2022
#This program will make two turtles that expand into two cyan balloons

import turtle

pearl = turtle.Turtle()
rachel = turtle.Turtle()
wn = turtle.Screen()
turtle.colormode(255)

pearl.backward(100)
for i in range(0,255,10):
    pearl.forward(10)
    pearl.pensize(i)
    pearl.color(0,i,i)

rachel.backward(100)
rachel.left(90)
for i in range(0,255,10):
    rachel.forward(10)
    rachel.pensize(i)
    rachel.color(0,i,i)

wn.exitonclick()