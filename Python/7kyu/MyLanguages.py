#My Languages
#https://www.codewars.com/kata/5b16490986b6d336c900007d

def my_languages(results):
    results = {k: v for k, v in sorted(results.items(), key= lambda x: x[1], reverse=True)}
    ans = []
    for key, val in results.items():
        if val>=60:
            ans.append(key)

    return ans
