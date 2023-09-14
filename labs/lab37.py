#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 5, 2022
#This program will draw a flower

import turtle
pearl = turtle.Turtle()

def flowerRecursion(pearl, n):
   if n > 0:
      pearl.forward(100)
      pearl.left(105)
      pearl.forward(52)
      pearl.left(105)
      pearl.forward(100)
      pearl.right(170)
   
      flowerRecursion(pearl, n - 1)

def main():
    flowerRecursion(pearl, 9)

if __name__ == '__main__':
   main()