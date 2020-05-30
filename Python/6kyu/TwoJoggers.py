#Two Joggers
#https://www.codewars.com/kata/5274d9d3ebc3030802000165

def nbr_of_laps(x, y):
    if x==y:
        return (1, 1)

    a = set([i*x for i in range(1,y+1)])
    b = set([i*y for i in range(1,x+1)])

    min_common = min(a.intersection(b))
    return (min_common/x, min_common/y)
