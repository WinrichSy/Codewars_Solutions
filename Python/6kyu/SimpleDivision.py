#Simple division
#https://www.codewars.com/kata/59ec2d112332430ce9000005

import math

def prime_factors(n):
    primes = []
    while(n%2==0):
        primes.append(2)
        n = n//2

    for i in range(3, n, 2):
        if i>n:
            break
        while(n%i==0 and n>1):
            primes.append(i)
            n = n//i

    return primes

def solve(a,b):
    if a==[] and b==[]:
        return True

    a_primes = list(set(prime_factors(a)))
    b_primes = list(set(prime_factors(b)))
    if a_primes == b_primes:
        return True

    elif a_primes==[] or b_primes==[]:
        return False

    for i in b_primes:
        if a%i!=0:
            return False

    return True
