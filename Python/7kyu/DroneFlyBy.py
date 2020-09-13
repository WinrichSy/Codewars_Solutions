#Drone Fly-By
#https://www.codewars.com/kata/58356a94f8358058f30004b5

def fly_by(lamps, drone):
    spot = drone.index('T')+1
    if spot>len(lamps):
        return 'o'*len(lamps)
    return 'o'*(spot)+lamps[spot:]
