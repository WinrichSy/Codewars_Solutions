#Total Amount of Points
#https://www.codewars.com/kata/5bb904724c47249b10000131

def points(score):
    total = 0
    for i in score:
        if(int(i[0])>int(i[-1])):
            total+=3
        elif(int(i[0])==int(i[-1])):
            total+=1

    return total
