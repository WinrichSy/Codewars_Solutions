#Cryptanalysis Word Patterns
#https://www.codewars.com/kata/5f3142b3a28d9b002ef58f5e

def word_pattern(word):
    letters = []
    ans = []
    for i in word.lower():
        if i not in letters:
            letters.append(i)
        ans.append(str(letters.index(i)))

    return '.'.join(ans)
