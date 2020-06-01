#Capitals first!
#https://www.codewars.com/kata/55c353487fe3cc80660001d4

def capitals_first(text):
    words = text.split()
    front = [i for i in words if i[0].isupper()]
    back = [i for i in words if i[0].islower()]
    return ' '.join(front + back)
