# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 18:35:14 2021

@author: Roger
Largest palindrome product
Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(number):
    n = str(number)
    y = -1
    count = 0
    half = int(len(n) / 2)
    for x in range(0, half):
        if n[x] != n[y]:
            return False
        else:
            count += 1
            y -= 1
            if count == half:
                return True


a = 999
palindromes = []
palinMults = {}
while a > 99:
    b = 999
    while b > 99:
        testN = a * b
        if is_palindrome(testN):
            palindromes.append(testN)
            palinMults[str(testN)] = [a, b]
            b -= 1
        else:
            b -= 1
    a -= 1

keyCode = str(max(palindromes))
x1 = palinMults[keyCode][0]
y1 = palinMults[keyCode][1]
print("\n\nLargest palindrome from multiplying two 3-digit numbers is:\n",
      keyCode, "\n - obtained by multiplying ", x1, " by ", y1)

""" Result: 906609

    Largest palindrome from multiplying two 3-digit numbers is:
    906609
            - obtained by multiplying  913  by  993
"""
