#Find the Capitals
#https://www.codewars.com/kata/53573877d5493b4d6e00050c

def capital(capitals):
    ans = []
    for i in capitals:
        vals = list(i.values())
        ans.append("The capital of {} is {}".format(vals[0], vals[1]))
    return ans
