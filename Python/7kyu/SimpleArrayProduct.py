#Simple Array Product
#https://www.codewars.com/kata/5d0365accfd09600130a00c9

import itertools
import numpy as np

def solve(arr):
    combinations = [np.product(i) for i in list(itertools.product(*arr))]
    return max(combinations)
