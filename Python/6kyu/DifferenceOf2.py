#Difference of 2
#https://www.codewars.com/kata/5340298112fa30e786000688

def twos_difference(lst):
    lst = sorted(lst)
    diffs = []
    i = 0
    while(i<len(lst)):
        curr = lst[i]
        if curr+2 in lst:
            diffs.append((curr, curr+2))
        i+=1

    return diffs
