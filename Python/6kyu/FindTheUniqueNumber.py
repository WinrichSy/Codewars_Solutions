#Find the Unique Number
#https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    set_arr = set(arr)
    for i in set_arr:
        if arr.count(i) == 1:
            return i
