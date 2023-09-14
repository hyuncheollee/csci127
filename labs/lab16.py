#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 16, 2022
#This program will ask the user for a list of names
#It will then print it out in a specific format

start = input("Enter a list of names, seperated by a semicolon: ")
cut = start.split(';')
length = len(cut)
fullName = ""
    
for i in range(length):
    cutAgain = cut[i].split(' ')
    print(cut[i][0:1] + ". " + cutAgain[1])