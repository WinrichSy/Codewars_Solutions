#Find array
#https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055

def find_array(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return []

    arr2 = [i for i in arr2 if i < len(arr1)]
    return [arr1[i] for i in arr2]
