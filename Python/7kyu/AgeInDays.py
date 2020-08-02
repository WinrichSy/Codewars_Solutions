#Age In Days
#https://www.codewars.com/kata/5803753aab6c2099e600000e

from datetime import date

def age_in_days(year, month, day):
    difference = ((date.today()-date(year, month, day)).__str__()).split()
    return('You are {} days old'.format(difference[0]))
