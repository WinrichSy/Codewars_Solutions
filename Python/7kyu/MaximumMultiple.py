#Maximum Multiple
#https://www.codewars.com/kata/5aba780a6a176b029800041c

def max_multiple(divisor, bound):
    for i in range(bound, 1, -1):
        if i%divisor == 0:
            return i
