###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.

c = float(input("Enter temperature in Celsius: "))

k = c + 273.15
f = c * 9/5 + 32

print(f'Temperature in Kelvin: {k}')
print(f'Temperature in Fahrenheit: {f}')