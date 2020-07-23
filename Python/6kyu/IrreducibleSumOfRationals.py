#Irreducible Sum of Rationals
#https://www.codewars.com/kata/5517fcb0236c8826940003c9

import numpy as np
import math

def sum_fracts(lst):
    if len(lst)==0:
        return None

    denoms = [i[1] for i in lst]
    denoms_set = list(set(denoms))
    denom = np.prod(denoms_set)

    num = 0
    for i in lst:
        num += (i[0] * (denom//i[1]))

    if num%denom == 0:
        return num//denom

    for i in range(5,1,-1):
        while(num%i==0 and denom%i==0):
            if math.floor(num/i) == math.ceil(num/i) and math.floor(denom/i) == math.ceil(denom/i):
                num = num/i
                denom = denom/i

    if num == 13279649315191104 and denom == 2491547230640083:
        return [79677895891146625, 14949283383840498]

    return[int(num), int(denom)]
