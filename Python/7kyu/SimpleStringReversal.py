#Simple string reversal
#https://www.codewars.com/kata/5a71939d373c2e634200008e

def solve(s):
    spaces = [i for i in range(len(s)) if s[i] == ' ']
    s = [i for i in s if i != ' ']
    ans = list(s[::-1])
    for i in spaces:
        ans.insert(i, ' ')

    return ''.join(ans)
