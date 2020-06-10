#Reversing a Process
#https://www.codewars.com/kata/5dad6e5264e25a001918a1fc

import string

def decode(r):
    alphabet = string.ascii_lowercase
    number = int(''.join([i for i in r if i.isnumeric()]))
    code = [i for i in r if i.isalpha()]
    if number%2==0:
        return 'Impossible to decode'
    ans = ''

    for i in code:
        index = alphabet.index(i)
        for j in range(26):
            if j*number%26 == index:
                ans += alphabet[j]
                break

    if len(set(ans)) == 2:
        return 'Impossible to decode'
    return ans
