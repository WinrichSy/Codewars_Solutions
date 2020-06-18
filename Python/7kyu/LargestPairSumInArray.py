#Largest Pair Sum in Array
#https://www.codewars.com/kata/556196a6091a7e7f58000018

def largest_pair_sum(numbers):
    numbers = sorted(numbers)
    ans = numbers[-2]+numbers[-1]
    return ans
