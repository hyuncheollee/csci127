#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 9, 2022
#This program will do something with movies

import pandas as pd 
import matplotlib.pyplot as mpl

csv = "movie_locations.csv"
movies = pd.read_csv(csv)

popular = int(input("order of most popular neighborhoods in movies: "))
print(movies["Neighborhood"].value_counts()[:popular])

directors = int(input("order of directors/filmmakers making most movies in NYC: "))
print(movies["Director/Filmmaker Name"].value_counts()[:directors])