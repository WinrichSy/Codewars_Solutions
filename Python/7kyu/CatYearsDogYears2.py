#Cat Years, Dog Years 2
#https://www.codewars.com/kata/5a6d3bd238f80014a2000187

def owned_cat_and_dog(cat_years, dog_years):
    cat_human_years = 0
    cat_years -= 15
    if cat_years >= 0:
        cat_human_years += 1
    cat_years -= 9
    if cat_years >= 0:
        cat_human_years += 1
    while(cat_years >= 0):
        cat_years -= 4
        if cat_years>=0:
            cat_human_years += 1

    dog_human_years = 0
    dog_years -= 15
    if dog_years >= 0:
        dog_human_years += 1
    dog_years -= 9
    if dog_years >= 0:
        dog_human_years += 1
    while(dog_years >= 0):
        dog_years -= 5
        if dog_years>=0:
            dog_human_years += 1
    return [cat_human_years, dog_human_years]
