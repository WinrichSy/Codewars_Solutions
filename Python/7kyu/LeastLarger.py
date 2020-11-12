#Least Larger
#https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4

def least_larger(a, i):
    curr_min = max(a)

    if a[i] == curr_min: return -1
    ans = 0
    for idx, val in enumerate(a):
        if val > a[i] and val <= curr_min:
            ans = idx
            curr_min = val

    return ans
