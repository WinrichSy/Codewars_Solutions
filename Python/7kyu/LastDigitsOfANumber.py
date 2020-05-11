#Last digits of a number
#https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0

def solution(n,d):
    if d <= 0:
        return []
    str_n = str(n)
    if d >= len(str_n):
        return [int(i) for i in str_n]

    ans = [int(i) for i in (str_n[-d:])]
    return ans
