#Reflecting Light
#https://www.codewars.com/kata/5eaf88f92b679f001423cc66

def gcd(x, y):
    if (x==0):
        return y
    elif (y==0):
        return x

    if (x>y):
        return gcd(x-y, y)
    return gcd(x, y-x)

def reflections(max_x,max_y):
    denom = gcd(max_x, max_y)
    return (max_x/denom + max_y/denom)%2 == 0
