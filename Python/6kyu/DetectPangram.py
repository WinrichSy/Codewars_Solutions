#Detect Pangram
#https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string
import re
def is_pangram(s):
    s = s.lower()
    return ''.join(sorted(''.join(list(set(re.sub('[^a-z]+', '', s)))))) == string.ascii_lowercase
