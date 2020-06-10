#Find the Mine!
#https://www.codewars.com/kata/528d9adf0e03778b9e00067e

def mineLocation(field):
    row_column = []
    row = 0
    for idx, val in enumerate(field):
        if 1 in val:
            row_column.append(idx)
            row = val

    for idx, val in enumerate(row):
        if val == 1:
            row_column.append(idx)

    return row_column
