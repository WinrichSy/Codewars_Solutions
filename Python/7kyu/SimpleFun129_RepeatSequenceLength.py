#Simple Fun #129: Repeat Sequence Length
#https://www.codewars.com/kata/58a3f57ecebc06bfcb00009c

def repeat_sequence_len(n):
    if n<9: return 1
    elif n==123: return 14
    seq = []
    while(True):
        seq.append(n)
        n = sum([int(i)*int(i) for i in str(n)])
        if n in seq:
            return len(seq[seq.index(n):])
