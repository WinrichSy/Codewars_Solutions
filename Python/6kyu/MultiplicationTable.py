#Multiplication Table
#https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08

def multiplication_table(size):
    ans = []
    for i in range(1, size+1):
        row = []
        for j in range(1, size+1):
            row.append(i*j)
        ans.append(row)

    return ans
