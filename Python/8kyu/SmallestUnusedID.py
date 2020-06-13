#Smallest unused ID
#https://www.codewars.com/kata/55eea63119278d571d00006a

def next_id(arr):
    arr = list(set(arr))
    ans = 0
    for i in sorted(arr):
        if ans == i:
            ans += 1
        else:
            return ans

    return ans
