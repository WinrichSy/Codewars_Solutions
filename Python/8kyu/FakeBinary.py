#Fake Binary
#https://www.codewars.com/kata/57eae65a4321032ce000002d

def fake_bin(x):
    ans = ''
    for i in x:
        if int(i)<5:
            ans += '0'
        else:
            ans += '1'
    return ans
