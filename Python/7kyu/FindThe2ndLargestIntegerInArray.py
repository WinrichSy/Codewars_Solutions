#Find the 2nd Largest Integer in Array
#https://www.codewars.com/kata/55a58505cb237a076100004a

def find_2nd_largest(arr):
    arr = sorted([i for i in set(arr) if isinstance(i, int)])
    if len(arr) <= 1:
        return None

    return arr[-2]
