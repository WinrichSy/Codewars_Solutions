#Count Letters in String
#https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d

import collections

def letter_count(s):
    s = collections.Counter(list(s.lower()))
    return s
