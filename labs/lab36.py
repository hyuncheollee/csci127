#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 5, 2022
#This program will compute price

def computePrice(liquid, size):
    price = -1.0
    
    if (liquid == "coffee"):
        if (size == "small"):
            price = 2.5
        elif (size == "medium"):
            price = 2.75
        elif (size == "large"):
            price = 3.00

    elif (liquid == "misto"):
        if (size == "small"):
            price = 3.15
        elif (size == "medium"):
            price = 3.35
        elif (size == "large"):
            price = 3.7
    
    elif (liquid == "mocha"):
        if (size == "small"):
            price = 3.5
        elif (size == "medium"):
            price = 3.8
        elif (size == "large"):
            price = 4.25
    
    elif (liquid == "tea"):
        if (size == "small"):
            price = 2.35
        elif (size == "medium"):
            price = 2.45
        elif (size == "large"):
            price = 2.90
            
    return price

def main():
    order = input("What would you like to drink? ")
    orderCut = input.split(' size ')
    size = orderCut[0]
    drink = orderCut[1]
    print(size, "size", drink, computePrice(drink, size))

if __name__ == "__main__":
    main()