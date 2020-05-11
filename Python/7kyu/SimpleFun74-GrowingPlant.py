#Simple Fun #74: GrowingPlant
#https://www.codewars.com/kata/58941fec8afa3618c9000184

def growing_plant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight<1:
        return 1
    curr = 0
    days = 0
    while(curr<desiredHeight):
        curr += upSpeed
        days += 1
        if curr >= desiredHeight:
            return days
        curr -= downSpeed
