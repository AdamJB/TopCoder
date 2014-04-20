#!/usr/bin/env python

"""
  Problem : BadNeighbors
  Code by : AdamJB
"""

class BadNeighbors:

  def maxDonations(self, v):
    if (len(v) <= 2):
      return max(v)

    md = [0 for _ in range(0, len(v))]
    mdL = [[] for _ in range(0, len(v))]

    maxDon = 0

    md[0] = v[0]
    mdL[0].append(0)    
    mdL[1].append(1)

    if md[0] >= v[1]:
      md[1] = md[1]
    else:
      md[1] = v[1]

    last = len(v)-1
    for i in range(2, len(v)):    
      x = v[i] + md[i-2]
      y = (md[i-1] - v[i-1]) + v[i]
      if i is last and 0 in mdL[i-2]:
        x -= v[0]        
      if i is last and 0 in mdL[i-1]:
        y -= v[0]        
      mdL[i].append(i)
      
      if y > x:
        md[i] = y
        mdL[i].extend(mdL[i-1])
        mdL[i].remove(i-1)
      else:        
        md[i] = x
        mdL[i].extend(mdL[i-2])    
    return max(md)


seq = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#seq = [10, 3, 2, 5, 7, 8]

sBadNeigh = BadNeighbors()
print sBadNeigh.maxDonations(seq)