#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 17, 2022
#This program will find perfect numbers

def sum(number):
    sum = 0
    for i in range(1, number - 1):
        if (number % i == 0):
            sum += i
    return sum

def numberTester(number):
    if (int(number) == sum(int(number))):
        return True
    else:
        return False

def main():
    number = input("Enter a perfect number: ")
    success = numberTester(number)
    while(not success):
        number = input(number + " is not a perfect number. Re-enter: ")
        success = numberTester(number)
    print("Congratulations! " + number + " is a perfect number.")               
    
if __name__ == "__main__":
    main()