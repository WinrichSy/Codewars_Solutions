#Cat years, Dog years
#https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b

def human_years_cat_years_dog_years(human_years):
    dog_years = 0
    cat_years = 0
    years = human_years - 1
    if years >= 0:
        dog_years += 15
        cat_years += 15
    years -= 1
    if years >= 0:
        dog_years += 9
        cat_years += 9
    if years >= 0:
        dog_years += years*5
        cat_years += years*4

    return [human_years, cat_years, dog_years]
