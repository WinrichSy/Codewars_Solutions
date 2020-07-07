#Encrypt This!
#https://www.codewars.com/kata/5848565e273af816fb000449

def flip(sub_word):
    if len(sub_word) == 1:
        return sub_word
    return sub_word[-1] + sub_word[1:-1] + sub_word[0]

def encrypt_process(word):
    flipped = ''
    if len(word)>1:
        flipped = flip(word[1:])
    encrypted = str(ord(word[0])) + flipped
    return encrypted

def encrypt_this(text):
    if text == '':
        return ''
    words = text.split(' ')
    ans = [encrypt_process(word) for word in words]
    return ' '.join(ans)
