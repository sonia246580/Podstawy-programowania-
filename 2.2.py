###
# The program simulates five dice rolls.
#
import random
print("Dice rolling simulator")
for i in range(5):
    dice_roll = random.randint(1,6)
    print(dice_roll, end=" ")

sum1 = 3 * 2 + 1 
print("sum1", sum1)

sum2 = 5 + 10 * 5 
print("sum2", sum2)

sum3 = 4 + 4 / 2 ** 2 
print("sum3", sum3)

sum4 = 4 % 3 % 2 % 1
print("sum4", sum4)

sum5 = 1 + 2 % 3 ** 4 * 5
print("sum5", sum5)

sum6 = True != False
print("sum6", sum6)
