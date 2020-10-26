#Valid Spacing
#https://www.codewars.com/kata/5f77d62851f6bc0033616bd8

def valid_spacing(s):
    if s=='': return True
    for i in range(0, len(s[:-1])):
        if s[i]==' ' and s[i+1]==' ':
            return False
    return s[0]!=' ' and s[-1]!=' '

#OR

def valid_spacing(s):
    return s == ' '.join(s.split())
