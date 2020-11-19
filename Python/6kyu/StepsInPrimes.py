#Steps in Primes
#https://www.codewars.com/kata/5613d06cee1e7da6d5000055

import math
def step(g, m, n):
    for i in range(m, n+1):
        ##if even, not prime
        if i%2==0:
            continue

        maximum = math.ceil(math.sqrt(i))
        if i%maximum==0:
            continue

        prime_bool = True
        for j in range(3, maximum+1, 2):
            if i%j==0:
                prime_bool = False
                break

        #check if its prime and if number+step is a prime
        if prime_bool:
            check_prime = i+g

            check_prime_bool = True
            check_prime_maximum = math.ceil(math.sqrt(check_prime))
            for j in range(3, check_prime_maximum+1, 2):
                if check_prime%j==0 or check_prime%2==0:
                    check_prime_bool = False
                    break

            #if number+g is prime and less than n, then return already.
            #or keep going to find the next one
            if check_prime_bool and i+g<=n:
                return [i, i+g]

    return None
