#Getting MAD
#https://www.codewars.com/kata/593a061b942a27ac940000a7

import itertools

def subtract(a_list):
    return a_list[0]-a_list[1]

def getting_mad(arr):
    possible_perms = [abs(subtract(i)) for i in list(itertools.permutations(arr, 2))]
    print(possible_perms)
    return min(possible_perms)
