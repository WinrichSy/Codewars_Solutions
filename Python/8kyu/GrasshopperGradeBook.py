#Grasshopper - Grade Book
#https://www.codewars.com/kata/55cbd4ba903825f7970000f5

def get_grade(s1, s2, s3):
    mean = (s1+s2+s3)/3
    if 100>=mean and mean>=90:
        return 'A'
    elif 90>mean and mean>=80:
        return 'B'
    elif 80>mean and mean>=70:
        return 'C'
    elif 70>mean and mean>=60:
        return 'D'
    return "F"
