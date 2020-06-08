#Replacement
#https://www.codewars.com/kata/598d89971928a085c000001a

def sort_number(a):
    val = 1
    while(a[a.index(max(a))] == val):
        val += 1
    a[a.index(max(a))] = val
    return sorted(a)
