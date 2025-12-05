###
# A program that prints your height both in cm and in feet and inches.
#

cm = int(input("Enter your height in centimeters: "))

total_inches = cm / 2.54
feet = int(total_inches // 12)
inches = int(total_inches % 12)

print(f'My height is {cm} cm, which is {feet} feet and {inches} inches.')