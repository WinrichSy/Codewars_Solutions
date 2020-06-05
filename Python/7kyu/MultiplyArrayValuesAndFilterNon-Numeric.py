#Multiply array values and filter non-numeric
#https://www.codewars.com/kata/55ed875819ae85ca8b00005c

def multiply_and_filter(seq, multiplier):
    ans = []
    for i in seq:
        if type(i)==float or type(i)==int:
            ans.append(i*multiplier)

    return ans
