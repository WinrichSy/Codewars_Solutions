#Holiday VI - Shark Pontoon
#https://www.codewars.com/kata/57e921d8b36340f1fd000059

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if shark_distance == 0:
        return 'Shark Bait!'
    if pontoon_distance == 0:
        return 'Alive!'
    if dolphin:
        if pontoon_distance/you_speed > shark_distance/(shark_speed/2):
            return 'Shark Bait!'
        else:
            return 'Alive!'
    if pontoon_distance/you_speed > shark_distance/shark_speed:
        return 'Shark Bait!'
    return 'Alive!'
