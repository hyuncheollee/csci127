#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 20, 2022
#You play a game with a computer

import random as r

def prompt():
    choice = int(input("Enter only 1-6: "))
    while (choice < 1 or choice > 6):
        print("Input needs to be in 1-6. Re-enter: ")
        choice = int(input("Enter only 1-6: "))
    return choice   

def sum(x, y):
    return x + y

def match(x, y):
    add = sum(x, y)
    if (add == 3 or add == 6 or add == 7 or add == 8):
        return True
    else:
        return False

def lazy(x, y):
    print("user: " + str(x))
    print("computer: " + str(y))
    if (x == y):
        print("draw")
    elif (match(x, y)):
        print("user wins")
    else:
        print("computer wins")
   
def main():
    userNum = prompt()
    computer = r.randrange(1, 6)
    lazy(userNum, computer)
    
    
if __name__ == "__main__":
    main()