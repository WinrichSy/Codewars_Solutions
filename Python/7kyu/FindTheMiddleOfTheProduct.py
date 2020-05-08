#Find the Middle of the Product
#https://www.codewars.com/kata/5ac54bcbb925d9b437000001

import numpy as np
import math
def find_middle(string):
    if not isinstance(string, str):
        return -1
    numbers = [int(i) for i in string if i.isnumeric()]
    if numbers == []:
        return -1
    total = np.prod(numbers)
    total_length = len(str(total))

    if total_length%2!=0:
        return int(str(total)[math.ceil(total_length/2)-1])
    elif str(total)[(total_length//2)-1] == '0':
        return int(str(total)[total_length//2])
    return int(''.join(str(total)[(total_length//2)-1:total_length//2+1]))
