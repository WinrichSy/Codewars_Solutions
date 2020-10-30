#Stones on the Table
#https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a

def solution(stones):
    count = 0
    curr = stones[0]
    for i in stones[1:]:
        if curr == i:
            count += 1
        else:
            curr = i
    return count
