#Maximum Product
#https://www.codewars.com/kata/5a4138acf28b82aa43000117

def adjacent_element_product(array):
    adjacent_products = []
    for idx, val in enumerate(array[:-1]):
        adjacent_products.append(val*array[idx+1])

    return max(adjacent_products)
