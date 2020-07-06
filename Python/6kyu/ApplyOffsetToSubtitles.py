#Apply Offset to Subtitles
#https://www.codewars.com/kata/5e454bf176551c002ee36486

from datetime import datetime

def subs_offset_apply(string, offset):
    sections = string.split()
    time1 = sections[0]
    time2 = sections[2]

    time1_sections = time1.split(':')
    time1_milliseconds = (3600000*int(time1_sections[0]))+(60000*int(time1_sections[1]))+(int(time1_sections[2].replace(',','')))
    if time1_milliseconds+offset < 0:
        return 'Invalid offset'
    time1_milliseconds += offset
    time1_hours = time1_milliseconds//3600000
    if time1_hours > 99:
        return 'Invalid offset'

    time2_sections = time2.split(':')
    time2_milliseconds = (3600000*int(time2_sections[0]))+(60000*int(time2_sections[1]))+(int(time2_sections[2].replace(',','')))
    if time2_milliseconds+offset < 0:
        return 'Invalid offset'
    time2_milliseconds += offset
    time2_hours = time2_milliseconds//3600000
    if time2_hours > 99:
        return 'Invalid offset'

    sections[0] = (str(datetime.fromtimestamp(time1_milliseconds/1000).strftime('%H:%M:%S,%f'))[:-3])
    sections[2] = (str(datetime.fromtimestamp(time2_milliseconds/1000).strftime('%H:%M:%S,%f'))[:-3])

    if time1_hours>9:
        sections[0] = str(time1_hours) + sections[0][2:]
    if time2_hours>9:
        sections[2] = str(time2_hours) + sections[2][2:]


    return ' '.join(sections)
