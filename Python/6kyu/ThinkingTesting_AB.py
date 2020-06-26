#Thinking & Testing: A*B?
#https://www.codewars.com/kata/5a90c9ecb171012b47000077

def test_it(a, b):
    a = sum([int(i) for i in str(a)])
    b = sum([int(i) for i in str(b)])
    return a*b
