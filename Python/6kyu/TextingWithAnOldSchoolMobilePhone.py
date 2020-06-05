#Texting with an old-school mobile phone
#https://www.codewars.com/kata/5ca24526b534ce0018a137b5

keypad = {'1':['.', ',', '?', '!'],
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z'],
            '0':[' '],
            '*':["'",'-','+','=']}

def send_message(message):
    buttons_pressed = []
    lower_case = True
    for i in message:
        if i.isupper() and i.isalpha() and lower_case:
            buttons_pressed.append('#')
            lower_case = False
        elif i.islower() and i.isalpha() and not lower_case:
            buttons_pressed.append('#')
            lower_case = True

        if i == ' ':
            if len(buttons_pressed)>0 and '0' in buttons_pressed[-1]:
                buttons_pressed.append(' ')
            buttons_pressed.append('0')

        elif i == '#':
            buttons_pressed.append('#')
            buttons_pressed.append('-')

        else:
            for key, val in keypad.items():
                if i.lower() in val:
                    if len(buttons_pressed)>0 and key in buttons_pressed[-1]:
                        buttons_pressed.append(' ')
                    buttons_pressed.append(key*(val.index(i.lower())+1))

                elif i.lower() in key:
                    if len(buttons_pressed)>0 and key in buttons_pressed[-1]:
                        buttons_pressed.append(' ')
                    buttons_pressed.append(key)
                    buttons_pressed.append('-')



    return ''.join(buttons_pressed)
