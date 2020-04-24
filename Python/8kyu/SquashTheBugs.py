#Squash the bugs
#https://www.codewars.com/kata/56f173a35b91399a05000cb7

def find_longest(string):
    spl = string.split(" ")
    longest = 0
    for i in spl:
      if(len(i) > longest):
        longest = len(i)
    return longest
