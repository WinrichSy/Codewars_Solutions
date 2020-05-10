#Happy Birthday, Darling!
#https://www.codewars.com/kata/5e96332d18ac870032eb735f

import math
def womens_age(n):
    base = n//2
    age = 20
    if n%2==1:
        age += 1
    return("{}? That's just {}, in base {}!".format(n, age, base))
