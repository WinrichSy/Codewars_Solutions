#Descending Order
#https://www.codewars.com/kata/5467e4d82edf8bbf40000155

def Descending_Order(num):
    if num < 10:
        return num

    num_as_string = str(num)
    num_list = []
    for i in num_as_string:
        num_list.append(int(i))

    #sort then reverse
    num_list.sort()
    num_list.reverse()

    total = 0
    for i in num_list:
        total = (total*10)+i

    return total
