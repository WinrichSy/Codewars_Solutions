#Basic Sequence Practice
#https://www.codewars.com/kata/5436f26c4e3d6c40e5000282

def sum_of_n(n):
    ans = []
    curr = 0
    for i in range(abs(n)+1):
        curr += i
        ans.append(curr)

    if n<0:
        ans = [-i for i in ans]
    return ans
