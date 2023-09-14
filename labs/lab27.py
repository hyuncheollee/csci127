#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: October 26, 2022
#This program will plot covid information

import matplotlib.pyplot as mpl
import pandas as pd

inputName = input("Enter a csv file: ")
borough = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
outputName = input("Enter output name: ")

cases = pd.read_csv(inputName)

min = cases[borough].min()
max = cases[borough].max()
mean = round(cases[borough].mean(), 3)
median = cases[borough].median()
stanDev = round(cases[borough].std(), 3)
cases["Fraction"] = cases[borough] / cases["case_count"]

graph = cases.plot(x = "date_of_interest", y = "Fraction")

print("Min:", min)
print("Max:", max)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", stanDev)
print("Fraction:", cases["Fraction"])

fig = mpl.gcf()
fig.savefig(outputName)

#covid_daily_cases.csv
#queensCovidFraction.png