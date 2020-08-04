#Mumbling
#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    ans = []
    for idx, val in enumerate(s):
        ans.append((val*(idx+1)).title())

    return '-'.join(ans)
