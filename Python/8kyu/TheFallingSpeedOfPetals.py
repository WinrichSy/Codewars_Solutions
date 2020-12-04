#The Falling Speed of Petals
#https://www.codewars.com/kata/5a0be7ea8ba914fc9c00006b

def sakura_fall(v):
    petal_height = 5*80
    if v <= 0: return 0
    return petal_height/v
