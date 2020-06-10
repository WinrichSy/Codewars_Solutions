#Simplify the number!
#https://www.codewars.com/kata/5800b6568f7ddad2c10000ae

def simplify(number):
    ans = []
    if number == 0:
        return ''

    num_as_str = str(number)
    num_length = len(num_as_str)
    for i in range(0, num_length):
        if int(num_as_str[i])>0:
            tens = 10**(num_length-i-1)
            if tens>1:
                ans.append(str(num_as_str[i]) + '*' + str(tens))
            else:
                ans.append(str(num_as_str[i]))

    return "+".join(ans)
