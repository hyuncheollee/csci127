#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 26, 2022
#This program will ask the user for an input
#It will then shrink and then reverse that sentence

string = input("Enter a phrase: ")
words = string.split(" ")
length = len(words)

for j in range(length, 0, -1):
    print(' '.join(words[:j]))

for i in range(2, length + 1):
        print(' '.join(words[:i]))
