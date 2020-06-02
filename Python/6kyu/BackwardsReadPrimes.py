#Backwards Read Primes
#https://www.codewars.com/kata/5539fecef69c483c5a000015

import math
# backwardsPrime is renamed backwards_prime
def backwards_prime(start, stop):
    primes = []
    for i in range(start, stop+1):
        bool_prime = True
        #checks forward and backwards is an even number immediately
        backwards = int(str(i)[::-1])

        if i%2==0 or backwards%2==0 or i==backwards:
            continue

        #goes to check the initial and backwards is divisible by their sqrt
        maximum = math.ceil(math.sqrt(i))
        maximum_backwards = math.ceil(math.sqrt(backwards))
        if i%maximum==0 or backwards%maximum_backwards==0:
            continue

        for j in range(3, maximum+1,2):
            if i%j==0:
                bool_prime = False
                break

        #skips checking the backwards if its not prime
        if not bool_prime:
            continue

        #BACKWARDS
        for j in range(3, maximum_backwards+1, 2):
            if backwards%j==0:
                bool_prime = False
                break

        if bool_prime:
            primes.append(i)

    return primes
