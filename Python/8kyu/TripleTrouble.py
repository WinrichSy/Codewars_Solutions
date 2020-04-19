#Triple Trouble
#https://www.codewars.com/kata/5704aea738428f4d30000914

def triple_trouble(one, two, three):
    word =''
    for i in range(len(one)):
        word += one[i]+two[i]+three[i]
    return word
