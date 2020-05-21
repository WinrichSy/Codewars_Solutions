#Unique String Characters
#https://www.codewars.com/kata/5a262cfb8f27f217f700000b

def solve(a,b):
    ans = ''
    for i in a:
        if i not in b:
            ans += i
    for i in b:
        if i not in a:
            ans += i

    return ans
