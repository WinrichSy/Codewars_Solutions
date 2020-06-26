#Read a UPC/Barcode
#https://www.codewars.com/kata/5b7dfd8cbfae24e5f200004d

def barcode_format(barcode):
    barcode.insert(11, ' ')
    barcode.insert(6, ' ')
    barcode.insert(1, ' ')
    return barcode

def read_barcode(barcode):
    binary = ''.join(['1' if i=='▍' else '0' for i in barcode])
    binary = binary[3:][:-3]
    left = ''
    left_bin = binary[:6*7]
    for i in range(0,6*7,7):
        left += str(LEFT_HAND[left_bin[i:i+7]])

    right = ''
    right_bin = binary[(6*7)+5:]

    for i in range(0,6*7,7):
        right += str(RIGHT_HAND[right_bin[i:i+7]])

    return ''.join(barcode_format(list(left)+list(right)))
