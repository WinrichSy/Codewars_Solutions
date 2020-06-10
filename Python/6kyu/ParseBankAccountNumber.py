#Parse Bank Account Number
#https://www.codewars.com/kata/597eeb0136f4ae84f9000001

numbers = { ' _ | ||_|':0,
            '     |  |':1,
            ' _  _||_ ':2,
            ' _  _| _|':3,
            '   |_|  |':4,
            ' _ |_  _|':5,
            ' _ |_ |_|':6,
            ' _   |  |':7,
            ' _ |_||_|':8,
            ' _ |_| _|':9}


def parse_bank_account(bank_account):
    account_numbers = bank_account.split('\n')
    ans = []
    for i in range(0, len(account_numbers[0]), 3):
        word = account_numbers[0][i:i+3] + account_numbers[1][i:i+3] + account_numbers[2][i:i+3]
        ans.append(str(numbers[word]))

    return int(''.join(ans))
