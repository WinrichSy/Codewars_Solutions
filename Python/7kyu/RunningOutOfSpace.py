#Running Out of Space
#https://www.codewars.com/kata/56576f82ab83ee8268000059

def spacey(array):
    ans = ['']
    for i in array:
        ans.append(ans[-1]+i)

    return ans[1:]
