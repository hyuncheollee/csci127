#Name: Hyuncheol Lee
#Email: hyuncheol.lee47@myhunter.cuny.edu
#Date: September 6, 2022
#This program will ask for things such as your first name, last name, and your email username
#It will then output all the inputs in certain formats

name = input("Enter name in format firstName lastName: ")
nameCut = name.split(' ')

firstName = nameCut[0]
lastName = nameCut[1]

print("name in LASTNAME, firstName format:", lastName.upper() + ",", firstName)

emailUser = input("Enter username of email: ")
emailAddress = "@hunter.cuny.edu"
print("email:", emailUser.lower() + emailAddress)