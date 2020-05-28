#The Vowel Code
#https://www.codewars.com/kata/53697be005f803751e0015aa

vowels = {'a':'1',
          'e':'2',
          'i':'3',
          'o':'4',
          'u':'5'}

numbers = {'1':'a',
          '2':'e',
          '3':'i',
          '4':'o',
          '5':'u'}

def encode(st):
    return ''.join([vowels[i] if i in vowels.keys() else i for i in st])

def decode(st):
    return ''.join([numbers[i] if i in numbers.keys() else i for i in st])
