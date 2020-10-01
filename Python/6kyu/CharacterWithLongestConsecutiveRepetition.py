#Character with longest consecutive repetition
#https://www.codewars.com/kata/586d6cefbcc21eed7a001155

def longest_repetition(chars):
    if chars=='': return ('', 0)
    char, max = chars[0], 1
    count = 1
    curr = chars[0]
    for i in chars[1:]:
        if curr == i:
            count += 1
            if count > max:
                max = count
                char = i
        else:
            count = 1
        curr = i

    return(char, max)
