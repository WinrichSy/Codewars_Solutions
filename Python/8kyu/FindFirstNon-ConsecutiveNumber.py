#Find the first non-consecutive number
#https://www.codewars.com/kata/58f8a3a27a5c28d92e000144

def first_non_consecutive(arr):
    cur = arr[0]
    for i in arr[1:]:
        if i != cur+1:
            return i
        cur += 1

    return None
