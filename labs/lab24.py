#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 17, 2022
#This program will ask for a list of words and then 
#It will count how many start / end with a or b 

list = input("Enter a list of words, seperated by a space: ")
amount = list.split()
length = len(amount)
ending = 0

print("number of words:", length)

for i in range(length):
    if (amount[i][len(amount[i]) - 1] == 'a' or amount[i][len(amount[i]) - 1] == 'b'):
        ending += 1
        
print("number of words ending with a or b:", ending)
print("fraction of words ending with a or b:", round(ending / length, 2))