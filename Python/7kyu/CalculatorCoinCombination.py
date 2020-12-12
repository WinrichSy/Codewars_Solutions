#Calculator: Coin Combination
#https://www.codewars.com/kata/564d0490e96393fc5c000029

def coin_combo(cents):
    coins = [25, 10, 5, 1]
    ans = []
    for i in coins:
        ans.append(cents//i)
        cents = cents%i

    return ans[::-1]
