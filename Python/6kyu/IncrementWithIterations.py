#Increment with Iterations
#https://www.codewars.com/kata/5ecc16daa200d2000165c5b1

def increment(number, iterations, spacer):
    curr = 0
    number_len = len(str(number))
    while(iterations>0):
        curr = (curr+spacer)%number_len
        number += 10**(number_len-curr-1)
        if number_len < len(str(number)):
            curr += 1
        number_len = len(str(number))
        iterations-=1
        print(number)

    return number
