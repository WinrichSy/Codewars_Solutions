#Form The Largest
#https://www.codewars.com/kata/5a4ea304b3bfa89a9900008e

def max_number(n):
    return int(''.join(sorted(str(n),reverse = True)))
