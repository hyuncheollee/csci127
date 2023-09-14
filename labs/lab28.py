#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 26, 2022
#This program will plot covid information

import matplotlib.pyplot as mpl
import pandas as pd

choice = input("Enter a choice: \na. group by borough\nb. group by year\n")
kids = pd.read_csv('children_lead.csv')
afc = "affected_children"


if (choice == 'a'):    
    boro = kids.groupby('borough')
    average = boro[afc].mean()
    print("average number of affected children by borough")
    print(average)

    specific = input("Enter a borough ")
    sboro = boro.get_group(specific)
    average = sboro[afc].mean()
    min = sboro[afc].min()
    max = sboro[afc].max()
    
    print("average number of affected children of", specific, "is", average) 
    print("min number of affected children of", specific, "is", min)
    print("max number of affected children of", specific, "is", max)    
    
elif (choice == 'b'):
    year = kids.groupby('year')
    average = year[afc].mean()
    print("number of affected children by year")
    print(average)
    
    specific = input("Enter a year (2005 - 2016): ")
    syear = year.get_group(int(specific))
    average = syear[afc].mean()
    min = syear[afc].min()
    max = syear[afc].max()
    
    print("average number of affected children in", specific, "is", average)
    print("min number of affected children in", specific, "is", min)
    print("max number of affected children in", specific, "is", max)
        
else: 
    print("wrong choice")