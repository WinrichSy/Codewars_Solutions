#Yes No Yes No
#https://www.codewars.com/kata/573c84bf0addf9568d001299

def yes_no(arr, yes=True):
    if len(arr)==0:
        return []
    answer = []
    leftovers = []
    for i in arr:
        if yes:
            answer.append(i)
            yes = False
        elif not yes:
            leftovers.append(i)
            yes = True
    return answer + yes_no(leftovers,yes)
