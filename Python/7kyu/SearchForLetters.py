#Search for letters
#https://www.codewars.com/kata/52dbae61ca039685460001ae

import string

def change(st):
    lowercase = string.ascii_lowercase
    ans = ['0' for i in lowercase]
    st = st.lower()
    for i in st:
        try:
            ans[lowercase.index(i)] = '1'
        except:
            continue

    return ''.join(ans)
