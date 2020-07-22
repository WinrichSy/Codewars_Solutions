#Covered Pawns
#https://www.codewars.com/kata/597cfe0a38015079a0000006

side_cols = {'a': ['b'],
             'b': ['a','c'],
             'c': ['b','d'],
             'd': ['c','e'],
             'e': ['d','f'],
             'f': ['e','g'],
             'g': ['f','h'],
             'h': ['g']}

def covered_pawns(pawns):
    ans = 0
    covers = []
    for i in pawns:
        col = i[0]
        row = int(i[1])
        for j in side_cols[col]:
            covers.append(j+str(row+1))

    covers = list(set(covers))
    for i in covers:
        if i in pawns:
            ans += 1

    return ans
