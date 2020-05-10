#Graceful Tipping
#https://www.codewars.com/kata/5eb27d81077a7400171c6820

import math

def graceful_tipping(bill):
    if bill < 10:
        return math.ceil(bill*1.15)

    bill = math.ceil(bill*1.15)
    rounder = 5*(10**(len(str(bill))-2))
    return math.ceil(bill/rounder)*rounder
