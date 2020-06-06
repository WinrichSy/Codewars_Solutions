#Onion Array
#https://www.codewars.com/kata/59b2883c5e2308b54d000013

def is_onion_array(a):
    a_length = len(a) - 1
    first = a[:len(a)//2]
    second = a[len(a)//2:][::-1]
    for i in range(len(first)):
        if first[i]+second[i]>10:
            return False

    return True
