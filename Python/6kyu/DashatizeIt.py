#Dashatize It
#https://www.codewars.com/kata/58223370aef9fc03fd000071

def dashatize(num):
    if num==None: return 'None'
    num = abs(num)
    ans = ''.join([i if int(i)%2==0 else '-'+i+'-' for i in str(num)])
    return ans.replace('--','-').strip('-')
