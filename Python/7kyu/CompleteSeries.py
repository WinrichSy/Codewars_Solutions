#Complete Series
#https://www.codewars.com/kata/580a4001d6df740d61000301

def complete_series(seq):
    for i in seq:
        if seq.count(i) > 1:
            return [0]

    max_num = max(seq)
    return list(range(max_num+1))
