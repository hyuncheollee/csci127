#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 16, 2022
#This program is free of errors

""" printCities(cityList) prints out ONCE Ten biggest cities in the USA, then print every city on the list of cityList, one per line """
def printCities(cityList):
    for city in cityList:
        print("Ten biggest cities in the USA: ")
        print(city)
    print()
  
""" inList(cityList, city) checks if myCity is a city on the list and prints out a message accordingly """     
def inList(cityList, myCity):    
    found = False
    for city in cityList:
        if (city == myCity):
            found = True
            
    if (found):
        print(myCity + " is in the list of cities.")
    else:
        print(myCity + " is not in the list of cities.")
        
""" numCities(cityList) return a string of cities in the list"""                
def numCities(cityList):
    num = len(cityList)
    return "There are " + str(num) + " cities in the list."

def main():
    # A list of eight biggest cities in the USA 
    cityList = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]
    
    print("Eight biggest cities in the USA: ")
    for i in range(len(cityList)):
        print(cityList[i])
    print()

    inList(cityList, "New York")
    inList(cityList, "Los Angeles")          
    inList(cityList, "Washington DC")
    inList(cityList, "Seattle")
    
    print(numCities(cityList))

if __name__ == "__main__":
    main()