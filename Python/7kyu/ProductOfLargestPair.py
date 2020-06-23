#Product of Largest Pair
#https://www.codewars.com/kata/5784c89be5553370e000061b

def max_product(a):
    first_largest = 0
    second_largest = 0
    for i in a:
        if i > first_largest:
            second_largest = first_largest
            first_largest = i
        if i > second_largest and i < first_largest:
            second_largest = i

    return first_largest*second_largest
