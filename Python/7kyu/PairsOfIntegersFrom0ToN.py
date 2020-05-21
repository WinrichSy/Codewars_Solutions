#Pairs of integers from 0 to n
#https://www.codewars.com/kata/588e27b7d1140d31cb000060

import itertools

def generate_pairs(n):
    nums = range(n+1)
    ans = list(itertools.combinations_with_replacement(nums,2))

    return [list(i) for i in ans]
