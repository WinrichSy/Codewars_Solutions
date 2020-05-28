#Bouncing Balls
#https://www.codewars.com/kata/5544c7a5cb454edb3c000047

def bouncingBall(h, bounce, window):
    if h<=0 or (0>bounce or bounce>=1) or window>h:
        return -1

    bounces = 0
    while(h>window):
        h = h*bounce
        bounces += 1

    return 2*bounces-1
