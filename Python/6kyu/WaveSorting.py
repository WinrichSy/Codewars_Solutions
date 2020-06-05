#Wave Sorting
#https://www.codewars.com/kata/596f28fd9be8ebe6ec0000c1

def wave_sort(a):
    print('starting: ', a)
    a.sort()
    if len(a)>1:
        for i in range(len(a)):
            if i % 2 == 1:
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp

    else:
        pass
