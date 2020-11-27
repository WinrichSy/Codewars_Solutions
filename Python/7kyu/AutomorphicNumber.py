#Automorphic Number (Special Number Series #6)
#https://www.codewars.com/kata/5a58d889880385c2f40000aa

def automorphic(n):
    if str(n*n)[-len(str(n)):] == str(n):
        return 'Automorphic'

    return 'Not!!'

#OR

def automorphic(n):
    if str(n*n).endswith(str(n)):
        return 'Automorphic'

    return 'Not!!'
