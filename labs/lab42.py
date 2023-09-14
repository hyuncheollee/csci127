#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 16, 2022
#This program will pin all the hospitals in NYC

import folium
import pandas as pd

hospitals = pd.read_csv("nyc_hospitals.csv")
NYC = folium.Map(location = [40.75, -74.125], zoom_start = 10)

for index, row in hospitals.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Facility Name"]
    newMarker = folium.Marker([lat, lon], popup = name)
    newMarker.add_to(NYC)
    
fileName = input("Enter output file: ")
NYC.save(outfile = fileName)