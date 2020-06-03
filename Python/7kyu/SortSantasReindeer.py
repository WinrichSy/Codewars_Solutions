#Sort Santa's Reindeer
#https://www.codewars.com/kata/52ab60b122e82a6375000bad

def sort_reindeer(reindeer_names):
    tuple_names = []
    for i in reindeer_names:
        tuple_names.append(tuple(i.split(' ')))

    ans = sorted(tuple_names, key=lambda x:x[1])
    ans = [' '.join(i) for i in ans]
    return ans
