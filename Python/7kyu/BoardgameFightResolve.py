#Boardgame Fight Resolve
#https://www.codewars.com/kata/58558673b6b0e5a16b000028

def fight_resolve(defender, attacker):
    if ((defender.isupper() and attacker.isupper()) or (defender.islower() and attacker.islower())):
        return -1

    d = defender.lower()
    a = attacker.lower()
    if a == 'k':
        if (d in ['k','s','a']):
            return attacker
        else:
            return defender
    elif a == 's':
        if (d in ['k','s','p']):
            return attacker
        else:
            return defender
    elif a == 'p':
        if (d in ['k','a','p']):
            return attacker
        else:
            return defender
    elif a == 'a':
        if (d in ['s','a','p']):
            return attacker
        else:
            return defender
