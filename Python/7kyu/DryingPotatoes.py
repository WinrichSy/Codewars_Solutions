#Drying Potatoes
#https://www.codewars.com/kata/58ce8725c835848ad6000007

def potatoes(p0, w0, p1):
    diff = w0*(p0*.01)-w0*(p1*.01)
    weight_diff = w0-(w0*(p1*.01))

    return int(w0*(1-(diff/weight_diff))+.01)
