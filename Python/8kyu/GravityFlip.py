#Gravity Flip
#https://www.codewars.com/kata/5f70c883e10f9e0001c89673

def flip(d, a):
    if d=='R': return sorted(a)
    return sorted(a,reverse=True)
