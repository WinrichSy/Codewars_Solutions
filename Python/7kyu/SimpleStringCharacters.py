#Simple string characters
#https://www.codewars.com/kata/5a29a0898f27f2d9c9000058

def solve(s):
    ans = [0, 0, 0, 0]
    for i in s:
        if i.isupper():
            ans[0] += 1
        elif i.islower():
            ans[1] += 1
        elif i.isnumeric():
            ans[2] += 1
        else:
            ans[3] += 1
    return ans
