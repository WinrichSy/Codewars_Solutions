#Halving Sum
#https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d

def halving_sum(n):
    ans = 0
    while(n>1):
        ans += n
        n = n//2

    return ans+1
