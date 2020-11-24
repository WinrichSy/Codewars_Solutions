#Check the Exam
#https://www.codewars.com/kata/5a3dd29055519e23ec000074

def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] == '': continue
        elif arr2[i]==arr1[i]: score+=4
        else: score-=1

    return score if score>0 else 0
