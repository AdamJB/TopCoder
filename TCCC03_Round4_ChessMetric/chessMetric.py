#!/usr/bin/env python

"""
  Problem : Chess Metric TCCC O3
  Code by : AdamJB
"""

def printGrid(grid):
  for row in range(0, len(grid)):
    cols = [str(x) for x in grid[row]]
    print " ".join(cols)

class ChessMetric:

  def howMany(self, piSize, plStart, plEnd, piNumMoves):
    # Clockwise direction from 1 move, and L moves
    dx = [-1, -1, 0, 1, 1, 1, 0, -1,  -1, 1, 2, 2, 1, -1, -2, -2]
    dy = [0, 1, 1, 1, 0, -1, -1, -1,  2, 2, 1, -1, -2, -2, -1, 1]

    grid = [[[0 for _ in range(0, piNumMoves+1)] for _ in range(0, piSize)] for _ in range(0,piSize)]

    grid[plStart[0]][plEnd[1]][0] = 1

    for n in range(1, piNumMoves+1):
      for x in range(0, piSize):
        for y in range(0, piSize):
          for d in range(0, 16):
            # Neighbor positions
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and ny >= 0 and nx < piSize and ny < piSize:
              grid[nx][ny][n] += grid[x][y][n-1]
    return grid[plEnd[0]][plEnd[1]][piNumMoves]

cm = ChessMetric()
#print cm.howMany(3, [0,1], [1,0], 1)
print cm.howMany(3, [0,0], [0,0], 2)
