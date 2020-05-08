#Find the Divisors!
#https://www.codewars.com/kata/544aed4c4a30184e960010f4

import math

def is_prime(integer):
    if integer%2==0:
        return False

    maximum = math.ceil(math.sqrt(integer))+1
    for i in range(3, maximum, 2):
        if integer%i == 0:
            return False
    return True

def divisors(integer):
    if is_prime(integer):
        return("{} is prime".format(integer))

    divs = []
    maximum = math.ceil(integer/2)+1
    for i in range(2, maximum):
        if integer%i==0:
            divs.append(i)

    return divs
