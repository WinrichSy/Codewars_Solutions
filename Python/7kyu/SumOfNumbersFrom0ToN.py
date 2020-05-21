#Sum of numbers from 0 to N
#https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763

def show_sequence(n):
    if n<0:
        return '{}<0'.format(n)
    elif n==0:
        return '0=0'

    ans = [str(i) for i in range(n+1)]
    ans = '+'.join(ans)

    return '{} = {}'.format(ans,sum(range(n+1)))
