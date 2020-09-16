#Mr. Martingale
#https://www.codewars.com/kata/5eb34624fec7d10016de426e

def martingale(bank, outcomes):
    curr = 100
    money_outcome = []
    for i in outcomes:
        if i:
            money_outcome.append(curr)
            curr = 100
        else:
            money_outcome.append(-curr)
            curr*=2

    return bank+sum(money_outcome)
