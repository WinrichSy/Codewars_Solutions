#Indexed Capitalization
#https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1

def capitalize(s,ind):
    sorted_idx = ind.sort()
    answer =[]
    for idx, val in enumerate(s):
        if idx in ind:
            answer.append(val.upper())
        else:
            answer.append(val)
    return "".join(answer)
