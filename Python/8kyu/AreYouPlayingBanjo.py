#Are You Playing Banjo?
#https://www.codewars.com/kata/53af2b8861023f1d88000832

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r': return '{} plays banjo'.format(name)
    return '{} does not play banjo'.format(name)
