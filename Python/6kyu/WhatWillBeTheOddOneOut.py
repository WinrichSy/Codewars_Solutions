#What will be the odd one out?
#https://www.codewars.com/kata/55b080eabb080cd6f8000035

import collections
def odd_one_out(s):
    ans = []
    s_counter = collections.Counter(list(s))
    s_unique = list(dict.fromkeys(s[::-1]))
    s_unique = s_unique[::-1]

    for i in s_unique:
        if s_counter[i]%2==1:
            ans.append(i)

    return ans
