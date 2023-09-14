#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 1, 2022
#This program will greet you

time = int(input("Enter hour (in 24 hour time): "))

if time < 12: 
    print("Good morning")
    
elif time < 17:
    print("Good afternoon")
    
else:
    print("Good evening")