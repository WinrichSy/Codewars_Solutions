#Return a String's Even Characters
#https://www.codewars.com/kata/566044325f8fddc1c000002c

def even_chars(st):
    if len(st)<=1 or len(st)>100:
        return 'invalid string'

    ans = [i for i in st[1::2]]
    return ans
