#Backspaces in string
#https://www.codewars.com/kata/5727bb0fe81185ae62000ae3

def clean_string(s):
    ans = []
    for i in s:
        if i!='#':
            ans.append(i)
        elif i=='#' and len(ans)>0:
            ans.pop()

    return ''.join(ans)
