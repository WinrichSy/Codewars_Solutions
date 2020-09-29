#Multiplicative Persistence... What's special about 277777788888899?
#https://www.codewars.com/kata/5c942f40bc4575001a3ea7ec

import numpy as np

def per(n):
    if n<10: return []
    ans = []

    while(n>=10):
        n = np.prod([int(i) for i in str(n)])
        ans.append(n)

    return ans
