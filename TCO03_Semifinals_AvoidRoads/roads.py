#!/usr/bin/env python

"""
  Problem : Avoid Roads
  Code by : AdamJB
  WIP
"""

def printGrid(grid):
  for row in range(0, len(grid)):
    cols = [str(x) for x in grid[row]]
    print " ".join(cols)

class AvoidRoads:

  def numWays(self, W, H, B):
    grid = [[0 for _ in range(0, W+1)] for _ in range(0,H+1)]
    
    grid[0][0] = 0
    grid[1][0] = 1
    grid[0][1] = 1

    for w in range(0, W+1):
      for h in range(0, H+1):        
        if h > 0:
          grid[h][w] += grid[h-1][w]
        if w > 0:
          grid[h][w] += grid[h][w-1] 

    printGrid(grid)
    return grid[-1][-1]

w = 1
h = 1
bad = ["0 0 0 1", "6 6 5 6"]
roads = AvoidRoads()
print roads.numWays(w, h, bad)