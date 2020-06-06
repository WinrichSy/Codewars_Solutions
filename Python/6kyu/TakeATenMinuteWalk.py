#Take a Ten Minute Walk
#https://www.codewars.com/kata/54da539698b8a2ad76000228

def isValidWalk(walk):
    start_x = 0
    start_y = 0
    current_x = 0
    current_y = 0
    for i in walk:
        if i == 'e':
            current_x += 1
        elif i == 'w':
            current_x -= 1
        elif i == 'n':
            current_y += 1
        elif i == 's':
            current_y -= 1

    return current_x == start_x and current_y == start_y and len(walk)==10
