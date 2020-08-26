#Find the Sum of the roots of a Quadratic equation
#https://www.codewars.com/kata/57d448c6ba30875437000138

import math

def roots(a,b,c):
    if (b*b)-(4*a*c) < 0:
        return None
    one = (-b + (((b*b)-(4*a*c)))*(1/2))/(2*a)
    two = (-b - (((b*b)-(4*a*c)))*(1/2))/(2*a)
    return round(one+two, 2)
