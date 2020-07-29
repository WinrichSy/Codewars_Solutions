#Short Long Short
#https://www.codewars.com/kata/50654ddff44f800200000007

def solution(a, b):
    if len(a) < len(b):
        return a+b+a
    return b+a+b
