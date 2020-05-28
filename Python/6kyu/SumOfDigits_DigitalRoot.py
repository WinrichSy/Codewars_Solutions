#Sum of Digits / Digital Root
#https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    if n<10:
        return n

    n_list = str(n)
    n_list = map(int, n_list)

    return digital_root(sum(n_list))
