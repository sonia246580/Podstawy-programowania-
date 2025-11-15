###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a = ')
b = input('b = ')
c = input('c = ')

side_a = int(a)
side_b = int(b)
side_c = int(c)

volume = side_a * side_b * side_c
surface_area = 2*(side_a*side_b) + 2*(side_a*side_c) + 2*(side_b*side_c)
print(f' The volume is {volume}, the suface area is {surface_area}')