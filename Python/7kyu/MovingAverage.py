#Moving Average
#https://www.codewars.com/kata/5c745b30f6216a301dc4dda5

def moving_average(values,n):
    if n==0: return None

    ans = []
    for i in range(len(values)-n+1):
        ans.append(sum(values[i:i+n])/n)

    return ans if ans!=[] else None
