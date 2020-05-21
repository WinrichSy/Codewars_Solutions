#A Rule of Divisibility by 13
#https://www.codewars.com/kata/564057bc348c7200bd0000ff

def thirt(n):
    previous = 0
    while(previous!=n):
        previous = n
        int_divs = [(10**i)%13 for i in range(len(str(n)))]
        reverse_n = str(n)[::-1]

        total = 0
        for i in range(len(int_divs)):
            total += (int_divs[i]*int(reverse_n[i]))

        n = total

    return previous
