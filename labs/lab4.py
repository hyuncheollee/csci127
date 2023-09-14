#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 6, 2022
#This program draws the purina logo while changing color

import turtle
Pearl = turtle.Turtle()
Pearl.pensize(5)
Pearl.shape("circle")
wn = turtle.Screen()

for n in range(4):
    if (n == 0):
        Pearl.color("green")
    elif (n == 1):
        Pearl.color("blue")
    elif (n == 2):
        Pearl.color("cyan")
    elif (n == 3):
        Pearl.color("red")

    Pearl.forward(300)
    Pearl.right(90)
    Pearl.forward(100)
    Pearl.right(90)
    Pearl.forward(100)
    Pearl.right(90)

wn.exitonclick()