#Simple remove duplicates
#https://www.codewars.com/kata/5ba38ba180824a86850000f7

def solve(arr):
    arr = arr[::-1]
    ans = []
    for i in arr:
        if i not in ans:
            ans.append(i)

    return ans[::-1]
