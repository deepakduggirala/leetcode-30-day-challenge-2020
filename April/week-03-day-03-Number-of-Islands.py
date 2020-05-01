'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

'''
Iterating through the grid, find a cell whose value is 1 (land), starting from this cell recursively navigate through its neighbors visiting each only once.
When visitied, set cell value current island count. Visit a cell only if its value is 1.

When iterating through the grid increment island counter by 1 when a cell whose value 1 is found. 
'''

class Solution:
    def numIslands(self, grid):
      num_islands = 1
      grid = [[int(c) for c in row] for row in grid]
      NR = len(grid)
      if NR == 0:
        return 0
      NC = len(grid[0])
      # print(NR, NC)
      def unvisited_neighbors(row, col):
        t = [(max(row-1,0), col), (row, min(col+1, NC-1)), (min(row+1, NR-1), col), (row, max(col-1, 0))]
        # print(row, col, t)
        return [(x,y) for x,y in t if grid[x][y] == 1]

      for i in range(NR):
        for j in range(NC):
          if grid[i][j] == 1:
            num_islands = num_islands + 1
            neighbor_stack = []
            neighbor_stack.append((i, j))
            while len(neighbor_stack) > 0:
              (x,y) = neighbor_stack.pop()
              grid[x][y] = num_islands
              for nr,nc in unvisited_neighbors(x, y):
                neighbor_stack.append((nr, nc))
      return num_islands - 1


inputs = [
  [["1","1","0","0","0"]
  ,["1","1","0","0","0"]
  ,["0","0","1","0","0"]
  ,["0","0","0","1","1"]]
]

for i in inputs:
  print('num islands:', Solution().numIslands(i))