#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 1, 2022
#This program will graph internet users over the world

import pandas as pd
import matplotlib.pyplot as mpl

graph = pd.read_csv("country_internet.csv")
continents = graph.groupby("Continental region")
average = continents["NO. OF Internet Plans"].mean()
print(average)

print()

print("possible regions are")
print(continents.groups.keys())
specific = input("choose a region: ")
print("In region", specific)

sRegion = continents.get_group(specific)
number = sRegion["NO. OF Internet Plans"].count()
print("number of countries:", number)
max = sRegion["NO. OF Internet Plans"].max()
min = sRegion["NO. OF Internet Plans"].min()
print("maximum number of internet plans:", max)
print("minimum number of internet plans:", min)

fileName = input("Please enter output file name: ")
barGraph = sRegion.plot.bar("Country", "NO. OF Internet Plans")
mpl.gcf().subplots_adjust(bottom = 0.25)
mpl.xlabel("Country in " + specific)
mpl.ylabel("NO. OF Internet Plans")

figure = mpl.gcf()
figure.savefig(fileName)
#NORTHERN AMERICA
#internet_plans_northern_america.png