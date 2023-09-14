#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 16, 2022
#This program will pin Central Park

import folium

NYC = folium.Map(location = [40.75, -74.125], zoom_start = 10)
folium.Marker([40.7812, -73.9665], popup = "Central Park")
NYC.save("nyc_Central_Park.html")