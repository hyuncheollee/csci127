#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 1, 2022
#This program will graph internet users over the world

import pandas as pd
import matplotlib.pyplot as mpl

fileName = input("Enter output file name: ")
graph = pd.read_csv("country_internet.csv")
graph["Percentage"] = graph["Internet users"] / graph["Population"] * 100
max = round(graph["Percentage"].max(), 2)
graph.plot(x = "Country", y = "Percentage")
country = graph["Percentage"].idxmax()

print("maximum percentage of all countries:", graph["Country"][country], max, "%")
figure = mpl.gcf()
figure.savefig(fileName)