#Split Strings
#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    answer = []
    if len(s) == 0:
        return answer

    elif len(s)%2!=0:
        s += '_'

    for i in range(0, len(s), 2):
        answer.append(s[i:i+2])

    return answer
