#Almost Even
#https://www.codewars.com/kata/529e2e1f16cb0fcccb000a6b

def split_integer(num, parts):

    val = num//parts
    ans = [val for i in range(parts)]
    if num%parts == 0:
        return ans

    for i in range(num%parts):
        ans[i] += 1

    return sorted(ans)
