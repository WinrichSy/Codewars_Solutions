#Easy Line
#https://www.codewars.com/kata/56e7d40129035aed6c000632

def easyline(n):
  trow = [1]
  y = [0]
  for x in range(max(n,0)):
      trow=[l+r for l,r in zip(trow+y, y+trow)]

  trow = [i**2 for i in trow]
  return sum(trow)
