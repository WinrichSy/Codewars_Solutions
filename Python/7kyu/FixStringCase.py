#Fix string case
#https://www.codewars.com/kata/5b180e9fedaa564a7000009a

def solve(s):
    lower = 0
    for i in s:
        if i.islower():
            lower += 1

    upper = len(s)-lower
    if upper == lower or lower > upper:
        return s.lower()

    return s.upper()
