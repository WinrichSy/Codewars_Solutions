#Simple Sum of Pairs
#https://www.codewars.com/kata/5bc027fccd4ec86c840000b7

def solve(n):
    if n<10:
        return n
    n_length = len(str(n))
    ans = 9*(n_length-1)
    a = int(''.join(['9' for i in range(n_length-1)]))
    ans += sum([int(i) for i in str(n-a)])
    return ans
