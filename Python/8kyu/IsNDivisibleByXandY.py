#Is n divisible by x and y?
#https://www.codewars.com/kata/5545f109004975ea66000086

def is_divisible(n,x,y):
    if n%x==0 and n%y==0:
        return True
    else:
        return False
