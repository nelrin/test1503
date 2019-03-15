# Ecercise 1- Geodatenanalyse - und modellierungen
# Author: Nele Rindsfüser
# Date: 07.03.2019

# Ex1.1

# question for user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# calculation
years_miss = 10 - (age%10)
age_then = years_miss + age


print ("Dear {} in {} years you'll be {}." .format(name, years_miss, age_then))

#run


