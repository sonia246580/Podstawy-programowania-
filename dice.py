###
# The program simulates five dice rolls.
#
import random
print("Dice rolling simulator")
for i in range(5):
    dice_roll = random.randint(1,6)
    print(dice_roll, end=" ")


sum1 = 3 * 2 + 1
print("sum1 = ", sum1)

sum2 = 5 + 10 * 5
print("sum2 = ", sum2)

sum3 = 4 + 4 / 2 ** 2
print("sum3 = ", sum3)

sum4 = 4 % 3 % 2 % 1
print("sum4 = ", sum4)

sum5 = 1 + 2 % 3 ** 4 * 5
print("sum5 = ", sum5)

sum6 = True != False
print("sum6 = ", sum6)

a = 50
print(type(a))
b = 149.17
print(type(b))
c = 4 * 7
print(type(c))
d = 4.0 * 7
print(type(d))
e = "Krakow University of Economics"
print(type(e))
f = True
print(type(f))
g = 2 > 5
print(type(g))

company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees
print("company = ",type(company))
print(company)
print("phone = ",type(phone))
print(phone)
print("employees = ",type(employees))
print(employees)
print("remote_work = ",type(remote_work))
print(remote_work)
print("big_company = ",type(big_company))
print(big_company)
print("income = ",type(income))
print(income)
print("income_per_person = ",type(income_per_person))
print(income_per_person)

###
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
#
number1 = 71
number2 = 14
number3 = 84
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)

###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)

###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = speed_kmh/3.6
print(speed_kmh, "km/h = ", speed_ms, "m/s")

###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print(diagonal)

h1 = 1.83
d1 = 3.57 * (h1 ** 2)
print('The distance to the horizon = ', d1)

h2 = 20
d2 = 3.57 * (h2 ** 2)
print('The distance to the horizon = ', d2)

print("###############################")
###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)

print("World population: ", total)
print("Southen Hemisphere: ", south)
print("Southen Hemisphere in %: ", south/total*100)