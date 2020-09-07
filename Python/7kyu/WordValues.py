#Word Values
#https://www.codewars.com/kata/598d91785d4ce3ec4f000018

import string
alphabet = string.ascii_lowercase
def name_value(my_list):
    ans = []
    if len(my_list)==0: return []
    my_list = [i.replace(' ','') for i in my_list]

    for idx, substring in enumerate(my_list):
        total = 0
        if len(substring)!=0:
            for letter in substring:
                total += alphabet.index(letter) + 1
        ans.append(total*(idx+1))

    return ans
