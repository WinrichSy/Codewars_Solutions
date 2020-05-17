#Sum of odd numbers
#https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

def row_sum_odd_numbers(n):
    length = sum([i for i in range(1, n+1)])
    starting_idx = sum([i for i in range(n)])
    odd_nums = [i for i in range(1,length*2) if i%2!=0]
    return sum(odd_nums[starting_idx:starting_idx+n])
