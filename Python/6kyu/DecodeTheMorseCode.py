#Decode the Morse Code
#https://www.codewars.com/kata/54b724efac3d5402db00065e

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    key_list = list(MORSE_CODE.keys())
    val_list = list(MORSE_CODE.values())
    ans = []
    dots_and_dashes = morse_code.replace('  ', ' ')
    dots_and_dashes = dots_and_dashes.split(' ')
    for i in dots_and_dashes:
        if i=='':
            ans.append(' ')
        else:
            ans.append(val_list[key_list.index(i)])

    return (''.join(ans)).strip()
