#Simple Barcode Scanner
#https://www.codewars.com/kata/55f4ad47ada1dd22f1000088

L_DIGITS = {'0001101':0,
            '0011001':1,
            '0010011':2,
            '0111101':3,
            '0100011':4,
            '0110001':5,
            '0101111':6,
            '0111011':7,
            '0110111':8,
            '0001011':9}
R_DIGITS = {'1110010' :0,
            '1100110':1,
            '1101100':2,
            '1000010':3,
            '1011100':4,
            '1001110':5,
            '1010000':6,
            '1000100':7,
            '1001000':8,
            '1110100':9}
def barcode_scanner(barcode):
    barcode = barcode[3:-3]
    first_half = barcode[:7*6]
    second_half = barcode[7*6+5:]
    ans = ''
    for i in range(0, len(first_half), 7):
        ans += str(L_DIGITS[first_half[i:i+7]])
    for i in range(0, len(second_half), 7):
        ans += str(R_DIGITS[second_half[i:i+7]])

    return ans
