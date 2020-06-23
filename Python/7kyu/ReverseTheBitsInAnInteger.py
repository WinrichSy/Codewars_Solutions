#Reverse the bits in an integer
#https://www.codewars.com/kata/5959ec605595565f5c00002b

def reverse_bits(n):
    reversed_binary = (str(bin(n))[2:][::-1])
    return(int(reversed_binary,2))
