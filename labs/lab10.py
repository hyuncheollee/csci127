#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 22, 2022
#This program will ask the user for a phrase.
#It will then capitalize each letter of the reversed string.
#It will then get an abbreviation of the last letter of each word starting from the last word.

string = input("input: ")
split = string.split(" ", -1)
first = ""

for i in range(len(split)):
    first += split[i][0:1]

print("user reverse:", string[::-1])
print("user reverse upper:", string.upper()[::-1])
print("user abbreviation:", first.upper())
