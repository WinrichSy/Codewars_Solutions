#Sort rectangles and circles by area II
#https://www.codewars.com/kata/5a1ebc2480171f29cf0000e5

import math

def sort_by_area(seq):
    areas = []
    for i in seq:
        if type(i)==tuple:
            areas.append((i,(i[0]*i[1])))
        elif type(i) in (float, int):
            areas.append((i, math.pi*(i**2)))

    areas.sort(key = lambda x: float(x[1]))
    ans = [i[0] for i in areas]
    return ans
