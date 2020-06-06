#Separate The Wheat From The Chaff
#https://www.codewars.com/kata/5bdcd20478d24e664d00002c

def wheat_from_chaff(values):
    next_negative_position = len(values)-1
    while values[next_negative_position] > 0:
        next_negative_position -= 1
    for idx, val in enumerate(values):
        if idx >= next_negative_position:
            break
        if val > 0 :
            temp = values[next_negative_position]
            values[next_negative_position] = val
            values[idx] = temp
            while values[next_negative_position] > 0:
                next_negative_position -= 1


    return values
