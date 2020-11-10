#Who is the Killer?
#https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d

def killer(suspect_info, dead):
    for suspect, seen in suspect_info.items():
        for i in dead:
            if i not in seen:
                break
            return suspect
