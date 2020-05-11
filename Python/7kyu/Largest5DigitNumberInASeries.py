#Largest 5 Digit Number in a series
#https://www.codewars.com/kata/51675d17e0c1bed195000001

def solution(digits):
    highests = []
    for idx, val in enumerate(digits):
        if val == '9':
            highests.append(int(digits[idx:idx+5]))

    return max(highests)
