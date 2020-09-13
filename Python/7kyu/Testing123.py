#Testing 1-2-3
#https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9

def number(lines):
    return ["{}: {}".format(idx, val) for idx, val in enumerate(lines, 1)]
