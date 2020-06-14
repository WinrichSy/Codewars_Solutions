#Is There an Odd Bit?
#https://www.codewars.com/kata/5d6f49d85e45290016bf4718

def any_odd(x):
    binary_x = bin(x)[2:]
    reversed = str(binary_x)[::-1]
    for idx, val in enumerate(reversed):
        if idx%2 == 1 and val=='1':
            return 1

    return 0
