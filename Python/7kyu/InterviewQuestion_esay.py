#Interview Question (easy)
#https://www.codewars.com/kata/5b358a1e228d316283001892

def get_strings(city):
    city = list(city.lower().replace(' ',''))
    letters = {}
    for i in city:
        if i in letters.keys():
            letters[i] += '*'
        else:
            letters[i] = ':*'

    ans = ''
    for key, val in letters.items():
        ans += str(key)+str(val)+','

    return ans[:-1]
