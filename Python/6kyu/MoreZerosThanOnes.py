#More Zeros than Ones
#https://www.codewars.com/kata/5d41e16d8bad42002208fe1a

def more_zeros(s):
    binary = [format(ord(i),'b') for i in s]
    s_indexes = [True if i.count('0')>i.count('1') else False for i in binary]
    letters = [s[i] for i in range(len(s_indexes)) if s_indexes[i]]
    temp = []
    for i in letters:
        if i not in temp:
            temp.append(i)

    return temp
