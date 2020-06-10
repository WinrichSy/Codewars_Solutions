#One is the loneliest number
#https://www.codewars.com/kata/5dfa33aacec189000f25e9a9

def loneliest(number):
    list_numbers = str(number)
    if '1' not in list_numbers:
        return False

    loneliness = []
    for idx, val in enumerate(list_numbers):
        i_range = int(val)
        left_limit = idx - i_range
        if left_limit <= 0:
            left_limit = 0
        loneliness.append((val,list_numbers[left_limit:idx] + list_numbers[idx+1:idx+i_range+1]))

#     print('loneliness', loneliness)

    digit_loneliness = []
    for i in loneliness:
        sub_sum = 0
        for j in i[1]:
            sub_sum += int(j)

#         print('i: {}, sub_sum: {}'.format(i,sub_sum))
        digit_loneliness.append((i[0], sub_sum))

    min_val = min(digit_loneliness, key=lambda t: t[1])[1]

    for i in digit_loneliness:
        if i[1] == min_val:
            if i[0] == '1':
                return True

    return False
