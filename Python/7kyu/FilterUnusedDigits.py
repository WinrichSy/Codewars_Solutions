#Filter Unused Digits
#https://www.codewars.com/kata/55de6173a8fbe814ee000061

def unused_digits(*args):
    numbers = ''.join([str(i) for i in args])
    numbers = (sorted(set(numbers)))
    ans = ''
    for i in range(10):
        if str(i) not in numbers:
            ans += str(i)

    return ans
