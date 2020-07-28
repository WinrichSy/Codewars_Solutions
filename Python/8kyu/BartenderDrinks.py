#L1: Bartender, drinks!
#https://www.codewars.com/kata/568dc014440f03b13900001d

DRINKS = {'Jabroni':'Patron Tequila',
          'School Counselor':'Anything with Alcohol',
          'Programmer':'Hipster Craft Beer',
          'Bike Gang Member':'Moonshine',
          'Politician':'Your tax dollars',
          'Rapper':'Cristal'}

def get_drink_by_profession(param):
    return DRINKS.get(param.title(), 'Beer')
