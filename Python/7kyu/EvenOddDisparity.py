#Even Odd Disparity
#https://www.codewars.com/kata/59c62f1bdcc40560a2000060

def solve(a):
    even = sum([1 if (isinstance(i,int) and i%2==0) else 0 for i in a])
    odd = sum([1 if (isinstance(i,int) and i%2==1) else 0 for i in a])
    return even-odd
