#Nth Power Rules Them All!
#https://www.codewars.com/kata/58aed2cafab8faca1d000e20

def modified_sum(a, n):
    return sum([i**n for i in a])-sum(a)
