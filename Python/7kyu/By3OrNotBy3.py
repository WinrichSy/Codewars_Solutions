#By 3, or not by 3? That is the question...
#https://www.codewars.com/kata/59f7fc109f0e86d705000043

def divisible_by_three(st):
    total = sum(int(i) for i in st)
    return total%3==0
