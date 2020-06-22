#Digital Cypher vol 2
#https://www.codewars.com/kata/592edfda5be407b9640000b2

import string
letters = string.ascii_lowercase

def decode(code, key):
    ans = []
    key = list(map(int, str(key)))
    iter = 0
    key_len = len(key)
    for i in code:
        ans.append(letters[(i-key[iter])-1])
        iter += 1
        if iter == key_len:
            iter = 0

    return ''.join(ans)
