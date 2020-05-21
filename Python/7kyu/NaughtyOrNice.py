#Naughty or Nice?
#https://www.codewars.com/kata/52a6b34e43c2484ac10000cd

def get_nice_names(people):
    ans = []
    for i in people:
        if i['was_nice'] == True:
            ans.append(i['name'])
    return ans

def get_naughty_names(people):
    ans = []
    for i in people:
        if i['was_nice'] == False:
            ans.append(i['name'])
    return ans
