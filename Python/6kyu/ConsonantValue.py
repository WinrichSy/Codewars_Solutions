#Consonant Value
#https://www.codewars.com/kata/59c633e7dcc4053512000073

from string import ascii_lowercase
vowels = ['a','e','i','o','u']
def solve(s):
    seperated_subs = []
    sub = []
    i = 0
    while(i<len(s)):
        if s[i] not in vowels:
            sub.append(s[i])
            if s[i]==s[-1]:
                seperated_subs.append(sub)
        elif s[i] in vowels and len(sub)>0:
            seperated_subs.append(sub)
            sub = []
        i += 1

    max = 0
    for subs in seperated_subs:
        total = 0
        for letter in subs:
            total += ascii_lowercase.index(letter)+1

        if max < total:
            max = total

    return max
