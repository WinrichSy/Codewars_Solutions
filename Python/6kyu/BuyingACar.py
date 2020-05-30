#Buying a car
#https://www.codewars.com/kata/554a44516729e4d80b000012

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    old = startPriceOld
    new = startPriceNew
    perLoss = percentLossByMonth

    if old-new >= 0:
        return [0, old-new]

    months = 1
    old = old*(.01*(100-perLoss))
    new = new*(.01*(100-perLoss))
    curr_money = (months*savingperMonth)+(old-new)
    while(curr_money <0):
        if months%2!=0:
            perLoss += 0.5
        months +=1
        old = old*(.01*(100-perLoss))
        new = new*(.01*(100-perLoss))
        curr_money = (months*savingperMonth)+(old-new)

    return [months, int(round(curr_money))]
