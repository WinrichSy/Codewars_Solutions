#Simple Sequence Validator
#https://www.codewars.com/kata/553f01db29490a69ff000049

def validate_sequence(sequence):
    diff= sequence[0]-sequence[1]
    curr = sequence[0]
    for i in sequence[1:]:
        if curr-i!=diff: return False
        curr = i

    return True
