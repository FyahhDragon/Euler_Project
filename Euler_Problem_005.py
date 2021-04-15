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
    
232792560.0  x  1
116396280.0  x  2
77597520.0  x  3
58198140.0  x  4
46558512.0  x  5
38798760.0  x  6
33256080.0  x  7
29099070.0  x  8
25865840.0  x  9
23279256.0  x  10
21162960.0  x  11
19399380.0  x  12
17907120.0  x  13
16628040.0  x  14
15519504.0  x  15
14549535.0  x  16
13693680.0  x  17
12932920.0  x  18
12252240.0  x  19
11639628.0  x  20    
232792560  is the smallest number evenly divisible by all intergers from 1 to 20

"""
