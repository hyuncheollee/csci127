#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: November 16, 2022
#This program will map a buncha school things

import folium
import pandas as pd

inputFile = input("Enter the file you want read: ")
schools = pd.read_csv(inputFile)
NYC = folium.Map(location = [40.75, -74.125], zoom_start = 10)

print("Enter 1 for Borough/Community,")
print("2 for Grade Level / Age Group")
choice = int(input("Your choice: "))
afterSchool = "_after_school.html"

if (choice == 1):
    boroughs = schools.groupby("Borough/Community")
    print(boroughs.groups.keys())
    specific = input("Enter Borough/Community name: ")
    boro = boroughs.get_group(specific)
    
    for index, row in boro.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["Name"]
        marker = folium.Marker([lat, lon], popup = name)
        marker.add_to(NYC)
    
    lower = specific.lower()
    fixed = lower.replace(" ", "_").replace("/", "_")
    NYC.save(outfile = fixed + afterSchool)

elif (choice == 2):
    grade = schools.groupby("Grade Level / Age Group")
    print(grade.groups.keys())
    specific = input("Enter Grade Level / Age Group name: ")
    grade = grade.get_group(specific)
    
    for index, row in grade.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["Name"]
        marker = folium.Marker([lat, lon], popup = name)
        marker.add_to(NYC)
    
    lower = specific.lower()
    fixed = lower.replace(" ", "_").replace("/", "_")
    NYC.save(outfile = fixed + afterSchool)