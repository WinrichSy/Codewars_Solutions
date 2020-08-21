#Pluck
#https://www.codewars.com/kata/530017aac7c0f49926000084

def pluck(objs, name):
    ans = []
    for i in objs:
        try:
            ans.append(i[name])
        except:
            ans.append(None)
    return ans
