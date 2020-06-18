#How Many Days are we Represented in a Foreign Country?
#https://www.codewars.com/kata/58e93b4706db4d24ee000096

def days_represented(trips):
    days = []
    for i in trips:
        days += list(range(i[0], i[1]+1))

    return len(set(days))
