#A Wolf In Sheep's Clothing
#https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15

def warn_the_sheep(queue):
    if queue[-1] == 'wolf': return 'Pls go away and stop eating my sheep'

    return 'Oi! Sheep number ' + str(queue[::-1].index('wolf')) + '! You are about to be eaten by a wolf!'
