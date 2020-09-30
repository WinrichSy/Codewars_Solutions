#Longest Alphabet Substring
#https://www.codewars.com/kata/5a7f58c00025e917f30000f1

from string import ascii_lowercase

def longest(s):
    if s == '':
        return ''
    if len(s) == 1:
        return s

    ans = []
    curr = [s[0]]
    for i in s[1:]:
        idx = ascii_lowercase.index(i)
        if idx >= ascii_lowercase.index(curr[-1]):
            curr.append(i)
            if len(ans) < len(curr):
                ans = curr
        else:
            if len(ans) < len(curr):
                ans = curr
            curr = [i]

    return ''.join(ans)
