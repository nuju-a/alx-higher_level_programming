#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str (number)[-1]
digit = int(last)
if digit > 5:
    print(f'Last digit of {number} is {last} and is greater than 5')
elif (digit < 6) and (digit !=  0):
    print(f'Last digit of {number} is -{last} and'+" "
          'is less than 6 and not 0')
else:
    print(f'Last digit of {number} is 0 and is 0')
