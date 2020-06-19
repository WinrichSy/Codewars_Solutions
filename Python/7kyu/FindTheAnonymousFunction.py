#Find the Anonymous Function
#https://www.codewars.com/kata/55a12bb8f0fac1ba340000aa

def find_function(func,arr):
    function = 0
    for i in func:
        if callable(i):
            function = i

    return list(filter(function, arr))
