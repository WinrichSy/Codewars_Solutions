#Unlucky Days
#https://www.codewars.com/kata/56eb0be52caf798c630013c0

import datetime
def unlucky_days(year):
    ans = 0
    for i in range(1,13):
        if datetime.date(year,i,13).weekday() == 4:
            ans += 1
    return ans
