#Minimize Sum Of Array (Array Series #1)
#https://www.codewars.com/kata/5a523566b3bfa84c2e00010b

def min_sum(arr):
    arr = sorted(arr)
    ans = sum([arr[i]*arr[len(arr)-i-1] for i in range(len(arr)//2)])

    return ans
