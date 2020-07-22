#Does my number look big in this?
#https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic( value ):
    value_str = str(value)
    total = 0
    length = len(value_str)
    for i in value_str:
        total += int(i)**length


    return total==value
