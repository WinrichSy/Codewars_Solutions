#Mexican Wave
#https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(people):
    ans = []
    if len(people)==0: return ans
    for i in range(len(people)):
        if people[i]==' ': continue
        ans.append(people[:i]+people[i].capitalize()+people[i+1:])
    return ans
