# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 01:56:40 2021

@author: Roger

Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Note: didn't get a version that wasn't going to take months
(by rough calculation) to execute the computation,
until I realised I needed to escape the factor() search on
potential candidates as soon as I detected more than two factors...
maybe there's a way of integrating the is_prime() function directly into
factors() function because of this... will investigate further'

"""


def factors(n):
    factors = []
    for x in range(1, n + 1):
        y = n % x
        if y == 0:
            factors.append(x)
# cancel search for factors if not prime i.e. more than 2 found
            if len(factors) > 2:
                return factors
    return factors


def is_prime(n):
    f = factors(n)
    if len(f) == 2:
        return True
    else:
        return False


def reverse_detect_prime(n):
    i = 2
    while i < (int(n / 2) + 1):
        test = (n / i)
        if test == int(test):
            # print staement to show progress
            print("found a factor: ", test, ":divisor = ", i)
            # check if result is prime
            if test % 2 != 0:
                # print staement to show progress
                print("factor: ", test, " is not Even... checking for prime!!")
                testPrime = is_prime(int(test))
                if testPrime is True:
                    # print final result
                    print(test, " is the largest prime factor of ", n)
                    break
                else:
                    # print staement to show progress
                    print(test, " is odd but not prime")
        i += 1


reverse_detect_prime(600851475143)

""" Result:
    Largest Prime Factor of 600851475143 is 6857

    search path results starting with largest factor
    and checking if prime if not an even number:

found a factor:  8462696833.0 ...divisor =  71
factor:  8462696833.0 ...is not Even... checking for prime!!
8462696833.0  is odd but not prime
found a factor:  716151937.0 ...divisor =  839
factor:  716151937.0 ...is not Even... checking for prime!!
716151937.0  is odd but not prime
found a factor:  408464633.0 ...divisor =  1471
factor:  408464633.0 ...is not Even... checking for prime!!
408464633.0  is odd but not prime
found a factor:  87625999.0 ...divisor =  6857
factor:  87625999.0 ...is not Even... checking for prime!!
87625999.0  is odd but not prime
found a factor:  10086647.0 ...divisor =  59569
factor:  10086647.0 ...is not Even... checking for prime!!
10086647.0  is odd but not prime
found a factor:  5753023.0 ...divisor =  104441
factor:  5753023.0 ...is not Even... checking for prime!!
5753023.0  is odd but not prime
found a factor:  1234169.0 ...divisor =  486847
factor:  1234169.0 ...is not Even... checking for prime!!
1234169.0  is odd but not prime
found a factor:  486847.0 ...divisor =  1234169
factor:  486847.0 ...is not Even... checking for prime!!
486847.0  is odd but not prime
found a factor:  104441.0 ...divisor =  5753023
factor:  104441.0 ...is not Even... checking for prime!!
104441.0  is odd but not prime
found a factor:  59569.0 ...divisor =  10086647
factor:  59569.0 ...is not Even... checking for prime!!
59569.0  is odd but not prime
found a factor:  6857.0 ...divisor =  87625999
factor:  6857.0 ...is not Even... checking for prime!!
6857.0  is the largest prime factor of  600851475143
"""
