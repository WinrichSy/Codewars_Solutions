#A Rule of Divisibility by 7
#https://www.codewars.com/kata/55e6f5e58f7817808e00002e

def seven(m):
    steps = 1
    first_digits = 0
    last_digits = 0
    while(len(str(m))>2):
        first_digits = m//10
        last_digit = m%10
        m = first_digits-(2*last_digit)
        if m%7==0 and len(str(m))<2:
            return m, steps
        else:
            steps+=1

    return m, steps-1
