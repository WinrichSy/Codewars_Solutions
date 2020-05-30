#Get Root Property Name
#https://www.codewars.com/kata/598638d7f3a2c489b2000030

def get_root_property(dict_, value):
    print(dict_)
    for key, val in dict_.items():
        if isinstance(val, list):
            if value in val:
                return key
        elif isinstance(val, dict):
            if get_root_property(val, value):
                return key

    return None
