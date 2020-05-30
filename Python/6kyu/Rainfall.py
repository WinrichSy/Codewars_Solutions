#Rainfall
#https://www.codewars.com/kata/56a32dd6e4f4748cc3000006

import numpy as np
def mean(town, strng):
    towns_data = strng.split('\n')
    possible_towns = [i.split(':')[0] for i in towns_data]

    if town not in possible_towns:
        return -1

    town_data = []
    for i in towns_data:
       if town in i:
          town_data = i

    dates = "".join(town_data.split(':')[1:]).split(',')
    values = [float(i.split(' ')[1:][0]) for i in dates]

    return np.mean(values)

def variance(town, strng):
    towns_data = strng.split('\n')
    possible_towns = [i.split(':')[0] for i in towns_data]

    if town not in possible_towns:
        return -1

    town_data = []
    for i in towns_data:
       if town in i:
          town_data = i

    dates = "".join(town_data.split(':')[1:]).split(',')
    values = [float(i.split(' ')[1:][0]) for i in dates]

    return np.var(values)
