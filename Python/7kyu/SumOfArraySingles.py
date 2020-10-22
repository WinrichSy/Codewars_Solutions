#Sum of Array Singles
#https://www.codewars.com/kata/59f11118a5e129e591000134/train/python

def repeats(arr):
    return sum([i for i in arr if arr.count(i)==1])
