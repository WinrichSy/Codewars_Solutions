#Find Screen Size
#https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f

def find_screen_height(width, ratio):
    ratios = ratio.split(':')
    width_r = int(ratios[0])
    height_r = int(ratios[1])
    height = int(width*(height_r/width_r))
    return('{}x{}'.format(width,height))
