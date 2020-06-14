#Thinking & Testing: How many "Word"?
#https://www.codewars.com/kata/56eff1e64794404a720002d2

def next_letter(s):
    if s=='w':
        return 'o'
    elif s=='o':
        return 'r'
    elif s=='r':
        return 'd'
    elif s=='d':
        return 'w'

def testit(s):
    s = list(s.lower())
    word = ''.join([i for i in s if i in 'word'])
    words_only = []
    curr_letter = 'w'
    for i in word:
        if i == curr_letter:
            words_only.append(i)
            curr_letter = next_letter(curr_letter)

    return ''.join(words_only).count('word')
