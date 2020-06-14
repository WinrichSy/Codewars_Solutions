#Simple Fun #35: Different Squares
#https://www.codewars.com/kata/588805ca44c7e8c3a100013c

import numpy as np

def different_squares(matrix):
    possible_2by2 = []
    matrix = np.array(matrix)
    rows, columns = matrix.shape
    if rows == 1 or columns == 1:
        return 0

    for i in range(rows-1):
        for j in range(columns-1):
            submatrix = matrix[i:i+2, j:j+2].tolist()
            if submatrix not in possible_2by2:
                possible_2by2.append(submatrix)

    return len(possible_2by2)
