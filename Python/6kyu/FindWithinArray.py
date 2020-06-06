#Find within array
#https://www.codewars.com/kata/51f082ba7297b8f07f000001

def find_in_array(seq, predicate):
    for key, val in enumerate(seq):
        if(predicate(val, key)):
            return key
    return -1
