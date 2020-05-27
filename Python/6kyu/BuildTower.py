#Build Tower
#https://www.codewars.com/kata/576757b1df89ecf5bd00073b

def tower_builder(n_floors):
    max_width = (n_floors*2)-1

    ans = []
    for i in range(1, n_floors+1):
        stars = '*'*((i*2)-1)
        ans.append(stars.center(max_width, ' '))

    return ans
