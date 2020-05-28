#Sums of Parts
#https://www.codewars.com/kata/5ce399e0047a45001c853c2b

def parts_sums(ls):
    curr_total = sum(ls)
    sums = [curr_total]
    for i in range(len(ls)):
        curr_total -= ls[i]
        sums.append(curr_total)

    return sums
