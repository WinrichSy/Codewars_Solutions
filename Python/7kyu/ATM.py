#ATM
#https://www.codewars.com/kata/5635e7cb49adc7b54500001c

def solve(n):
    if n%10>0:
        return -1
    count = 0
    curr_nom = [500,200,100,50,20,10]
    i = 0
    while(n>0):
        if n>=curr_nom[i]:
            n-=curr_nom[i]
            count+=1
        else:
            i += 1

    return count
