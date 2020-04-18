'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
'''
Solution: Use Dijkstra
https://github.com/deepakduggirala/Algorithms/blob/master/Graph/Dijkstra.py
'''
import heapq

class Solution:
  def minPathSum(self, grid):
    NR = len(grid)
    if NR == 0:
      return 0
    NC = len(grid[0])
    if NC == 0:
      return 0
    
    S = (0,0) #start
    visited = {k: False for k in [(r,c)  for c in range(NC) for r in range(NR)]}
    distance = {k: float('inf') for k in [(r,c)  for c in range(NC) for r in range(NR)]}
    distance[S] = grid[0][0]
    heap = []
    heapq.heappush(heap, (0,S))

    def neighbors(u):
      ui,uj = u
      return [(grid[x][y], (x,y)) for x,y in [(min(ui+1, NR-1), uj), (ui, min(uj+1, NC-1))]]

    while len(heap) != 0:
      # while(True):
      #   _,u = heapq.heappop(heap)
      #   if not visited[u]:
      #     break
      _,u = heapq.heappop(heap)
      visited[u] = True

      for weight_uv,v in neighbors(u):
        if not visited[v]:
          if distance[v] > distance[u] + weight_uv:
            distance[v] = distance[u] + weight_uv
            heapq.heappush(heap, (distance[v], v))
    return distance[(NR-1, NC-1)]

inputs = [
  [
    [1,3,1],
    [1,5,1],
    [4,2,1]
  ]
]

for i in inputs:
  print(Solution().minPathSum(i))