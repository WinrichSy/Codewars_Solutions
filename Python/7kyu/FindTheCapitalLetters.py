#Find the capitals
#https://www.codewars.com/kata/539ee3b6757843632d00026b

def capitals(word):
    ans = []
    for idx, val in enumerate(word):
        if val.isupper():
            ans.append(idx)

    return ans
