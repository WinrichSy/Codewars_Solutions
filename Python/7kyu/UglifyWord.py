#Uglify Word
#https://www.codewars.com/kata/5ce6cf94cb83dc0020da1929

def uglify_word(s):
    ans = [s[0].upper()]
    for i in s[1:]:
        if i == '-':
            ans.append('-')
            continue
        elif ans[-1].isupper():
            ans.append(i.lower())
        else:
            ans.append(i.upper())

    return ''.join(ans)
