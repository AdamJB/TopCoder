#!/usr/bin/env python

"""
  Problem : Ellys Sorting Trimmer
  Code by : AdamJB
"""

class EllysSortingTrimmer:

  def getMin(self, S, L):
    stringSize = len(S)
    lString = [S[x] for x in xrange(stringSize)]

    if L == stringSize:
      lString = sorted(lString)
    else:
      start = stringSize - L
      for i in range(start+1, -1, -1):    
        f = sorted(lString[i:i+L])
        lString[i:i+L] = f
        # Pop Remaining
        lString[i+L:] = []
      
    return "".join(lString)


string = "ABRACADABRA"
strength  = 5

sTrimmer = EllysSortingTrimmer()
print sTrimmer.getMin(string, strength)