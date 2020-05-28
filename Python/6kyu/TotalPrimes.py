#Total Primes
#https://www.codewars.com/kata/5a516c2efd56cbd7a8000058

import math
import itertools

#Used for caching values
primed = {}

def is_prime(num):
    maximum = math.ceil(math.sqrt(num))
    if num%maximum == 0:
        return False
    for i in range(3, maximum, 2):
        if num%i == 0:
            return False
    return True

def get_total_primes(a, b):
    #Gets a list of possible combinations of viable answers
    a_len = len(str(a))
    b_len = len(str(b))
    prime_nums = ['2','3','5','7']
    list_of_nums = []
    for i in range(a_len, b_len+1):
        list_of_nums += itertools.product(prime_nums, repeat=i)
    list_of_nums = [int(''.join(i)) for i in list_of_nums]

    ans = []
    i = 0
    while(list_of_nums[i]<a):
        i+=1

    while(a<=list_of_nums[i] and list_of_nums[i]<b and i<len(list_of_nums)-1):
        #If answer is cached, just append it
        if list_of_nums[i] in primed or list_of_nums[i]==2:
            ans.append(list_of_nums[i])
            i+=1
            continue

        #Skips even numbers
        if list_of_nums[i]%2==0:
            i+=1
            continue

        #Will check if value is prime or not
        if is_prime(list_of_nums[i]):
            ans.append(list_of_nums[i])
            primed[list_of_nums[i]] = list_of_nums[i]
        i+=1

    return(len(ans))
