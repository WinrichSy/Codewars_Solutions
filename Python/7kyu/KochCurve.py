#Koch Curve
#https://www.codewars.com/kata/5c5abf56052d1c0001b22ce5

def koch_curve(n):
    if n==0: return []
    deep = koch_curve(n-1)
    return [*deep, 60, *deep, -120, *deep, 60, *deep]
