#Alternate capitalization
#https://www.codewars.com/kata/59cfc000aeb2844d16000075

def capitalize(s):
    answer = []
    letter =''
    for j in range(2):
        word = []
        for idx, val in enumerate(s):
            #upper start
            if j%2==0:
                if idx%2==0:
                    word.append(val.upper())
                elif idx%2==1:
                    word.append(val)
            else:
                if idx%2==1:
                    word.append(val.upper())
                elif idx%2==0:
                    word.append(val)
        answer.append(letter.join(word))
    return answer
