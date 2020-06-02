#Persistent Bugger
#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

import numpy as np
def persistence(n):
    total = 0
    while n>=10:
        n = np.prod([int(i) for i in list(str(n))])
        total+=1

    return total
