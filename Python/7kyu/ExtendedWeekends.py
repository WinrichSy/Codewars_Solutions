#Extended Weekends
#https://www.codewars.com/kata/5be7f613f59e0355ee00000f

import datetime

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def solve(a,b):
    ans = []
    for i in range(a, b+1):
        for j in [1,3,5,7,8,10,12]:
            d = datetime.date(i,j,1)
            if d.weekday()==4:
                ans.append(months[j-1])

    return (ans[0], ans[-1], len(ans))
