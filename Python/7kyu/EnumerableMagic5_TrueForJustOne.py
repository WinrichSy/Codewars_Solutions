#Enumerable Magic #5 - True for Just One?
#https://www.codewars.com/kata/54599705cbae2aa60b0011a4

def one(sq, fun):
    a = 0
    for i in sq:
        if fun(i):
            a+=1

    return a==1
