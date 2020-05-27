#Are they the "same"?
#https://www.codewars.com/kata/550498447451fbbd7600041c

def comp(array1, array2):
    if array1==None or array2==None:
        return False
    if array1 == [] and array2 == []:
        return True
    elif len(array1) != len(array2):
        return False
    a = sorted([abs(i) for i in array1])
    b = sorted(array2)
    for i in range(len(a)):
        if a[i]**2 != b[i]:
            return False

    return True
