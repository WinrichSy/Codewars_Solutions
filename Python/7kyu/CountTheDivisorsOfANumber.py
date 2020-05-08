#Count the divisors of a number
#https://www.codewars.com/kata/542c0f198e077084c0000c2e

def divisors(n):
    total = 0
    for i in range(1,n+1):
        if n%i==0:
            total+=1

    return total
