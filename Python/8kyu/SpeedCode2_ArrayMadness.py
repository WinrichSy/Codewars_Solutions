#SpeedCode #2 - Array Madness
#https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1

def array_madness(a,b):
    a = sum([i**2 for i in a])
    b = sum([i**3 for i in b])
    return a>b
