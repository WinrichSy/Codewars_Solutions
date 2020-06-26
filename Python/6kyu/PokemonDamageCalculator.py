#Pokemon Damage Calculator
#https://www.codewars.com/kata/536e9a7973130a06eb000e9f

def calculate_damage(your_type, opponent_type, attack, defense):
    multiplier = .5
    if your_type == opponent_type:
        return 50*(attack/defense)*multiplier
    #FIRE
    elif your_type == 'fire':
        if opponent_type == 'grass':
            multiplier = 2
        elif opponent_type == 'water':
            multiplier = .5
        elif opponent_type == 'electric':
            multiplier = 1
    #WATER
    elif your_type == 'water':
        if opponent_type == 'grass':
            multiplier = .5
        elif opponent_type == 'electric':
            multiplier = .5
        elif opponent_type == 'fire':
            multiplier = 2
    #GRASS
    elif your_type == 'grass':
        if opponent_type == 'electric':
            multiplier = 1
        elif opponent_type == 'water':
            multiplier = 2
        elif opponent_type == 'fire':
            multiplier = .5
    #ELECTRIC
    elif your_type == 'electric':
        if opponent_type == 'fire':
            multiplier = 1
        elif opponent_type == 'water':
            multiplier = 2
        elif opponent_type == 'grass':
            multiplier = 1
    return (50*(attack/defense))*multiplier
