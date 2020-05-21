#A Floating-Point System
#https://www.codewars.com/kata/5df754981f177f0032259090

def mant_exp(a_number, digits_number):
    str_a_number = str(a_number)
    extra = 0
    if 'E' in str_a_number:
        extra = int(str_a_number[str_a_number.index('E')+1:])
        str_a_number = str_a_number[:str_a_number.index('E')]

    point_idx = str_a_number.index('.')
    num_pos = 0
    for idx, val in enumerate(str_a_number):
        try:
            if int(val) > 0:
                num_pos = idx
                break
        except:
            continue

    p = point_idx - num_pos + extra
    p -= digits_number
    if point_idx < num_pos:
        p += 1

    str_a_number = str(int(str_a_number.replace('.', '') + ('0'*abs(p))))
    ans = str_a_number[:digits_number] +'P{}'.format(p)
    return(ans)
