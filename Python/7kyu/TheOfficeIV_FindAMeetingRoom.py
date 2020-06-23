#The Office IV - Find a Meeting Room
#https://www.codewars.com/kata/57f604a21bd4fe771b00009c

def meeting(rooms):
    try:
        return rooms.index('O')
    except:
        return 'None available!'
