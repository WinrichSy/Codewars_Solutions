#How Much
#https://www.codewars.com/kata/55b4d87a3766d9873a0000d4

def howmuch(m, n):
    boats = 7
    cars = 9
    #goal is to see how much money within range of m and n to get remainder of b=2 and c=1
    answer = []
    if m>n:
        temp = n
        n = m
        m = temp

    for i in range(m, n+1):
        if i < boats and i < cars:
            continue
        elif i%boats == 2 and i%cars ==1:
            answer.append(["M: {}".format(i), "B: {}".format(i//boats), "C: {}".format(i//cars)])

    return answer
