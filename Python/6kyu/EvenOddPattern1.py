#Even Odd Pattern #1
#https://www.codewars.com/kata/559e708e72d342b0c900007b

def even_odd(arr):
    answer = 0
    for i in range(len(arr)):
        if i%2==0:
            answer += arr[i]
        else:
            answer *= arr[i]

    return answer
