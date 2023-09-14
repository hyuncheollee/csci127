#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 1, 2022
#This program counts the occurrence of a letter in a string

def count(string, char):
    count = 0
    for i in range(len(string)):
        if (string[i] == char):
            count += 1
    return count

def main():
    sentence = input("Enter a string: ")
    character = input("Enter a char: ")
    print("number of '" + character + "' in \"" + sentence + "\" is", count(sentence, character))

if __name__ == "__main__":
    main()