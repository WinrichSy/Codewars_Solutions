#Life Path Number
#https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0

def life_path_number(birthdate):
    numbers = [int(i) for i in birthdate.replace('-','')]
    while(sum(numbers)>9):
        numbers = [int(i) for i in str(sum(numbers))]

    return sum(numbers)
