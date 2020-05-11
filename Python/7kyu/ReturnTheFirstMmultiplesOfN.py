#Return the first M multiples of N
#https://www.codewars.com/kata/593c9175933500f33400003e

def multiples(m, n):
    ans = []
    for i in range(1, m+1):
        ans.append(i*n)

    return ans
