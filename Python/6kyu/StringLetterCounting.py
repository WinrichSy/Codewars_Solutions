#String Letter Counting
#https://www.codewars.com/kata/59e19a747905df23cb000024

import collections
def string_letter_count(s):
    letters = sorted(list(set(s.lower())))
    cnt = collections.Counter(s.lower())

    stringletter = ''
    for i in letters:
        if i.isalpha():
            stringletter += '{}{}'.format(cnt[i],i)

    return stringletter
