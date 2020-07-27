#Delete occurences of an element if it occurs more than n times
#https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order,max_e):
    order_set = list(set(order))
    nums_to_remove = []
    for i in order_set:
        if order.count(i) > max_e:
            for j in range(max_e):
                nums_to_remove.append(i)

    opposite_order = order[::-1]
    for i in nums_to_remove:
        for j in range(opposite_order.count(i)-max_e):
            opposite_order.remove(i)

    return opposite_order[::-1]
