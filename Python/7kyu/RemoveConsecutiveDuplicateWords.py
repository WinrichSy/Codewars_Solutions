#Remove Consecutive Duplicate Words
#https://www.codewars.com/kata/5b39e91ee7a2c103300018b3

from itertools import groupby

def remove_consecutive_duplicates(s):
    words = s.split(' ')
    ans = [i[0] for i in groupby(words)]
    return ' '.join(ans)
