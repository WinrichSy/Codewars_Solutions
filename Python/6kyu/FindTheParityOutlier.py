#Find the Parity Outlier
#https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):

    odds = 0
    evens = 0
    outlier = 0

    for i in integers:
        if i%2 == 0:
            evens += 1
            if evens > 1:
                break
            
        elif i%2 == 1:
            odds +=1
            if odds > 1:
                break

    #look for odd number if more evens
    if evens > 1:
        for i in integers:
            if i%2==1:
                return i

    #look for even number if more odds
    elif odds > 1:
        for i in integers:
            if i%2==0:
                return i

    return outlier
