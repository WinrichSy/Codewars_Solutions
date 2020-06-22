#Alien Accent
#https://www.codewars.com/kata/5874657211d7d6176a00012f

def convert(st):
    ans = []
    for i in st:
        if i == 'o':
            ans.append('u')
        elif i == 'a':
            ans.append('o')
        else:
            ans.append(i)
    return "".join(ans)
