#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 6, 2022
#This program will ask the user for a phrase. It will then print out each character in that phrase
#its ASCII code, and then the next two letters in the ASCII table

phrase = input("Enter a phrase: ")
print("letter ASCII next_two_letter")
length = len(phrase)

number = [None] * length
for n in range(length):
    number[n] = ord(phrase[n])

nextTwo = [None] * length
for o in range(length):
    nextTwo[o] = chr(ord(phrase[o]) + 2)




for z in range(length):
   print("%6c %5i %15c" % (phrase[z], number[z], nextTwo[z]))

