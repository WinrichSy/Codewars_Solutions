#Find the odd int
#https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    seq_set = list(set(seq))
    for i in seq_set:
        if seq.count(i)%2!=0:
            return i
