#Abbreviate a Two Word Name
#https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3

def abbrevName(name):
    ans = [i[0].upper() for i in name.split()]
    return '.'.join(ans)
