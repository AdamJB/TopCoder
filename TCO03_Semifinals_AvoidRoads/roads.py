#!/usr/bin/env python

"""
  Problem : Avoid Roads TCO3 Semifinals 4
  Code by : AdamJB
"""

def printGrid(grid):
  for row in range(0, len(grid)):
    cols = [str(x) for x in grid[row]]
    print " ".join(cols)

def parseBad(bad):
  badPoints = []
  for b in bad:
    ints = [int(i) for i in b.strip().split()]
    badPoints.append(((ints[0], ints[1]), (ints[2], ints[3])))
  return badPoints

class AvoidRoads:

  def numWays(self, W, H, B):
    bp = parseBad(B)
    grid = [[0 for _ in range(0, W+1)] for _ in range(0,H+1)]

    e1 = ((0,0), (0,1))
    e2 = ((0,0), (1,0))
    grid[0][0] = 0
    if e2 not in bp:
      grid[1][0] = 1
    if e1 not in bp:
      grid[0][1] = 1

    for w in range(0, W+1):
      for h in range(0, H+1):
        if h > 0:
          edge1a = ((h, w), (h-1, w))
          edge1b = (edge1a[1],edge1a[0])
          if edge1a not in bp and edge1b not in bp:
            grid[h][w] += grid[h-1][w]
        if w > 0:
          edge2a = ((h, w), (h, w-1))
          edge2b = (edge2a[1],edge2a[0])
          if edge2a not in bp and edge2b not in bp:
            grid[h][w] += grid[h][w-1]

    # printGrid(grid)
    return grid[-1][-1]

w = 6
h = 6
bad = ["0 0 0 1", "6 6 5 6"]

# w = 2
# h = 2
# bad = ["0 0 1 0", "1 2 2 2", "1 1 2 1"]

w = 1
h = 1
bad = []

w = 35
h = 31
bad = []

roads = AvoidRoads()
print roads.numWays(w, h, bad)

