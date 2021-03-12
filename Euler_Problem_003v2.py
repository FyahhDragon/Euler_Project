# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 20:39:57 2021

@author: Roger


Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Note: version 2... integrated the check for primeness directly into
factors() function removing the is_prime() function'

"""


def factors(n):
    # search for factors to determine if prime
    factors = []
    for x in range(1, n + 1):
        y = n % x
        if y == 0:
            factors.append(x)
# cancel search for factors if not prime i.e. more than 2 found
            if len(factors) > 2:
                return False
    if len(factors) == 2:
        return True


def reverse_detect_prime(n):
    i = 2
    while i < (int(n / 2) + 1):
        test = (n / i)
        if test == int(test):
            # check if result is prime
            if test % 2 != 0:
                # check for primeness
                testPrime = factors(int(test))
                if testPrime is True:
                    # print final result
                    print(test, " is the largest prime factor of ", n)
                    break
                else:
                    print("searching for largest prime factor of:\n", n,
                          "\n found factor, checking if prime... please wait")
        i += 1


reverse_detect_prime(600851475143)

""" Result:
    Largest Prime Factor of 600851475143 is 6857
"""
