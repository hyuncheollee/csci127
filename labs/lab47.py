#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 18, 2022
#This program will guess your number

def oneTwoThree(input):
    input = int(input)
    if (input > 0 and input < 4):
        return True
    else:
        return False

def correctTest(choice):
    if (choice == 3):
        return True
    else:
        return False

def main():
    print("Pick an integer in [0, 100] in your mind.")
    options = "1: too small   2: too big   3: just right"
    enterChoice = "Enter choice 1-3: "
    correct = False
    guess = 1    
    start = 0
    end = 100   
    
    while(not correct):
        if (guess < 7):
            print("Guess " + str(guess) + ": is it " + str((start + end) // 2) + "?")
            print(options)
            choice = int(input(enterChoice))
            while (not oneTwoThree(choice)):
                choice = int(input(enterChoice))
            correct = correctTest(choice)
            guess += 1
            if (choice == 1):
                start = (start + end) // 2 + 1
            elif (choice == 2):
                end = (start + end) // 2 - 1
            elif (choice == 3):
                print("Congratulations! The answer is " + str((start + end) // 2))
                correct = True
        else:
            print("Guess 7: the answer must be " + str(end))
            correct = True
    
if __name__ == "__main__":
    main()