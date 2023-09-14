#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 6, 2022
#This program will ask the user for a phrase and then a number. It will then shift the original string to x amount of places.

sentence = input("Enter an all-small-letter string: ")
number = int(input("Enter a non-negative int to shift: "))
length = len(sentence)
answer = ""

for n in range(length):
    if (ord(sentence[n]) + number > 122):
        newNumber = ord(sentence[n]) + number
        newNumber = newNumber - 122
        answer += chr(96 + newNumber)
    else:
        answer += chr(ord(sentence[n]) + number)

print(answer)