#Sort the odd
#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    if len(source_array) == 0:
        return source_array
    cpy_array = []
    for i in source_array:
        if(i%2==1):
            cpy_array.append(i)

    cpy_array.sort()

    current_idx = 0
    for idx, elm in enumerate(source_array):
        if(elm%2==1):
            source_array[idx] = cpy_array[current_idx]
            current_idx += 1
    return source_array
