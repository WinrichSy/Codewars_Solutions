#Simple fibonacci strings
#https://www.codewars.com/kata/5aa39ba75084d7cf45000008

def solve(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '01'

    return solve(n-1) + solve(n-2)
