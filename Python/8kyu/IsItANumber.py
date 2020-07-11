#Is it a number?
#https://www.codewars.com/kata/57126304cdbf63c6770012bd

def isDigit(string):
    try:
        return isinstance(float(string), float)
    except:
        return False
