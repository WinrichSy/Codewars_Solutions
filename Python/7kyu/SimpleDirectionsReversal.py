#Simple Directions Reversal
#https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca

def opposite(arr):
    new_arr = []
    for i in arr:
        if i=='Right': new_arr.append('Left on ')
        elif i=='Left': new_arr.append('Right on ')
    new_arr.append('Begin on ')
    return new_arr

def solve(arr):
    if len(arr)==1:
        return arr

    directions = [i.split(' ')[0] for i in arr]
    directions = opposite(directions)
    directions = directions[::-1]

    streets = [' '.join(i.split(' ')[2:]) for i in arr][::-1]

    ans = []
    for idx, elm in enumerate(directions):
        ans.append(directions[idx] + streets[idx])

    return ans
