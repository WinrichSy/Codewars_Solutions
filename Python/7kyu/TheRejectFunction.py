#The reject() function
#https://www.codewars.com/kata/52988f3f7edba9839c00037d

def reject(seq, predicate):
    ans = []
    for i in seq:
        try:
            if predicate(i) == False:
                ans.append(i)
        except:
            continue

    return ans
