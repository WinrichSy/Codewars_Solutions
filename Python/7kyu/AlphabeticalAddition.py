#Alphabetical Addition
#https://www.codewars.com/kata/5d50e3914861a500121e1958

from string import ascii_lowercase

def add_letters(*letters):
    letters = [*letters]
    count = 0
    for i in letters:
        count += ascii_lowercase.index(i)

    return ascii_lowercase[(count+len(letters)-1)%26]
