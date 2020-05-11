#Responsible Drinking
https://www.codewars.com/kata/5aee86c5783bb432cd000018

def hydrate(drink_string):
    drinks = ''.join(drink_string.split(',')).split(' ')
    total = 0
    for i in drinks:
        try:
            total += int(i)
        except:
            continue

    if total == 1:
        return ('{} glass of water'.format(total))
    return ('{} glasses of water'.format(total))
