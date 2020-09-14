#Split By Value
#https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc

def split_by_value(k, elements):
    if k < min(elements): return elements

    a = [i for i in elements if i<k]
    b = [i for i in elements if i>=k]
    return a+b
