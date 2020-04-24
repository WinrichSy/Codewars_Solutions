#N-th Power
#https://www.codewars.com/kata/57d814e4950d8489720008db

def index(array, n):
    if n>len(array)-1:
        return -1

    return array[n]**n
