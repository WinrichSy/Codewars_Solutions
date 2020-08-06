#Simple String Division
#https://www.codewars.com/kata/5b83c1c44a6acac33400009a

def solve(st,k):
    length = len(st)-k
    combos = [int(st[i:i+length]) for i in range(len(st))]
    return max(combos)
