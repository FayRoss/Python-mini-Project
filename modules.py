
import calculations
print(calculations.y)
print(calculations.remainder(100,40))
print(calculations.add(18,17))

# 2nd syntax of importation - importing just one fxn
from calculations import add
a= int(input("Enter the first number"))
b= int(input("Enter the second number"))
print(add(a,b))

# 3rd syntax - using the alias name(all modules are imported)
import calculations as cal; 
a= int(input("Enter the first number"))
b= int(input("Enter the second number"))
print("sum=",cal.add(a,b))

print(cal.prime(60))

print(cal.checkanagram("race", "care"))

#4th syntax of imortation - importing a couple of fxns
from calculations import y,multi,prime,checkanagram
print(y)
print(multi(40,100))
print(prime(9))
print(checkanagram("Fay","Yaf"))

#5th synatx - importong only fxns
from calculations import*
print(remainder(20,2))
print(divide(10,2))

import calculations
print(dir(calculations))

# Inbuilt modules
import math
print(dir(math))

print(math.sin(90))
print(math.sqrt(4))
print(math.pow(8,2))
print(math.remainder(10,2))

import datetime
print(datetime.date.today())

import random
cars=["Honda","SUV", 'Mazda',"Subaru"]
choose=random.choice(cars)
print(choose)

