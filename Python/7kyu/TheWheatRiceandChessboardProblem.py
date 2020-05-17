#The wheat/rice and chessboard problem
#https://www.codewars.com/kata/5b0d67c1cb35dfa10b0022c7

def squares_needed(grains):
    if grains <= 1:
        return grains

    grain_ammount = [grains]
    while(grains>=2):
        grain_ammount.append(grains/2)
        grains = grains/2

    return len(grain_ammount)
