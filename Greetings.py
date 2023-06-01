#Write a program that asks the user to enter their name and their age. 
#Print out a message that greets them and that tells them the year that they will turn 100 years old

import datetime

name = input("Enter the name : ")
age = int(input("Ente the age : "))

current_year = datetime.datetime.now().year
year_to_100 = 100 - age
year_of_100 = current_year + year_to_100

print("Hello, "+ name + ' you will turn 100 years old in the year ' + str(year_of_100)+ ".")


