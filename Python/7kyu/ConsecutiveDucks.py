#Consecutive Ducks
#https://www.codewars.com/kata/5dae2599a8f7d90025d2f15f

import math
def consecutive_ducks(n):
    if n%2==1:
        return True

    return not math.log2(n).is_integer()
