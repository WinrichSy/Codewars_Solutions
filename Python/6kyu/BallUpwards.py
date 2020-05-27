#Ball Upwards
#https://www.codewars.com/kata/566be96bb3174e155300001b

import math
def max_ball(v0):
    v = v0*.277778
    g = 9.81
    t = 0
    h = 0.1
    while(h>=0):
        h = (v*(t/10))-(0.5*g*(t/10)*(t/10))
        t += 1

    return(math.ceil(t/2)-1)
