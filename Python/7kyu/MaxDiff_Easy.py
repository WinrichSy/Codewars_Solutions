#Max diff - easy
#https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095

def max_diff(lst):
    if len(lst) == 0:
        return 0
    lst = sorted(lst)
    return lst[-1] - lst[0]
