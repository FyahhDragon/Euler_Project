"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

div = 1
x = 20  # solution must be a multiple of 20

while div <= 20:
    if x % div == 0:
        if div == 20:
            for y in range(1, 21):
                print(x/y, " x ", y)
            print(x, " is the smallest number evenly divisible by all intergers from 1 to", div)
            break
        else:
            div += 1
    else:
        div = 1
        x += 20

"""
RESULT:
    
232792560  is the smallest number evenly divisible by all intergers from 1 to 20

"""
