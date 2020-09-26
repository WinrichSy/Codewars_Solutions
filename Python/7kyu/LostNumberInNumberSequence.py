#Lost Number in Number Sequence
#https://www.codewars.com/kata/595aa94353e43a8746000120

def find_deleted_number(arr, mixed_arr):
    return sum(arr)-sum(mixed_arr)
