#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 17, 2022
#This program will convert ft / cm / inch

print("(a) convert centimeters to feet")
print("(b) convert centimeters to feet and inches")
print("(c) convert feet and inches to centimeters")

choice = input("Enter a or b or c: ")

if (choice == 'a'):
    cm = input("Enter height in centimeters: ")
    feet = int(cm) / 30.48
    feet = round(feet, 2)
    print("height is", feet, "feet")
    
elif (choice == 'b'):
    cm = input("Enter height in centimeters: ")
    feet = int(cm) // 30.48
    inches = int(cm) % 30.48
    inches = inches / 2.54
    feet = round(feet)
    inches = round(inches)
    if (feet == 0):
        print("height is", inches, "inches")
    elif (inches == 0):
        print("height is", feet, "feet")
    else:
        print("height is", feet, "feet and", inches, "inches")
    
elif (choice == 'c'):
    feet, inches = input("Enter height in feet and inches, seperated by a space: ").split()
    feet = int(feet) * 12
    inches = int(inches) + feet
    cm = round(inches * 2.54)
    print("height is", cm, "cm")
    
else: 
    print("Wrong choice, please enter only a or b or c.")