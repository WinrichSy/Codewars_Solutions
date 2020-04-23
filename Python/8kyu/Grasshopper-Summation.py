#Grasshopper - Summation
#https://www.codewars.com/kata/55d24f55d7dd296eb9000030

def summation(num):
    total = 0
    while(num>0):
        total += num
        num -=1

    return total
