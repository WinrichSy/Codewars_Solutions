#Find the Nth Catalan Number
#https://www.codewars.com/kata/579637b41ace7f92ae000282

import math

def nth_catalan_number(n):
    if (n == 0 or n == 1):
        return 1

    catalan = [0 for i in range(n + 1)]
    catalan[0] = 1
    catalan[1] = 1

    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

    return catalan[n]
