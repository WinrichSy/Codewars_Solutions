#Split and then add both sides of an array together
#https://www.codewars.com/kata/5946a0a64a2c5b596500019a

def split_and_add(numbers, n):
    for i in range(n):
        if len(numbers)==1:
            return numbers
        half = len(numbers)//2
        a = numbers[:half]
        b = numbers[half:]

        if len(a) < len(b):
            a.insert(0,0)

        numbers = [a[i]+b[i] for i in range(len(a))]

    return numbers
