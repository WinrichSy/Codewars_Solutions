#Array Exchange
#https://www.codewars.com/kata/5353212e5ee40d4694001114

def exchange_with(a, b):
    reversed_a = a[::-1]
    reversed_b = b[::-1]
    for i in range(len(a)):
        a.pop()
    for i in range(len(b)):
        b.pop()
    for i in reversed_a:
        b.append(i)
    for i in reversed_b:
        a.append(i)
