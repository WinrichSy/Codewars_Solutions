#Return the Day
#https://www.codewars.com/kata/59dd3ccdded72fc78b000b25

weekdays = {1:'Sunday',
            2:'Monday',
            3:'Tuesday',
            4:'Wednesday',
            5:'Thursday',
            6:'Friday',
            7:'Saturday'}

def whatday(num):
    try:
        return weekdays[num]
    except:
        return 'Wrong, please enter a number between 1 and 7'
