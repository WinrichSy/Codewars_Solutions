#Ordered Count of Characters
#https://www.codewars.com/kata/57a6633153ba33189e000074

import collections

def ordered_count(inp):
    letters = collections.Counter(inp)
    ans = []
    for key, val in letters.items():
        ans.append((key, val))

    return ans
