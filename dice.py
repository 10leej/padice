import random
# set dice size, no number of dice here just assumes 1 die
num1 = random.randint(1,20)
num2 = random.randint(1,20)
# num2 is modifier
num3 = 12
sum = num1 + num2 + num3
print("Sum of {0}d{1} + {2} is {3}" .format(num1, num2, num3, sum))
