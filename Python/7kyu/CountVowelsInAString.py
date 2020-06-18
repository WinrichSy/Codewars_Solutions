#Count Vowels in a String
#https://www.codewars.com/kata/55b105503da095817e0000b6

def count_vowels(s = ''):
    if isinstance(s, str) != True:
        return None

    ans = 0
    s = s.lower()
    for vowel in 'aeiou':
        ans += s.count(vowel)

    return ans
