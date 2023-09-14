#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 17, 2022
#This program will count binary

input = input("Enter a string with 0 or 1 only: ")
index = len(input) - 1
number = 0
error = 0

for i in range(len(input)):
    if (input[i] == '1'):
        number += pow(2, index)
    elif (input[i] == '0'):
        number += 0
    elif (error == 1):
        print("Letter", input[i], "is not allowed allowed in binary string.")
        exit(0)
    else:
        error += 1
    index -= 1

if (error == 0):
    print("num =", number)