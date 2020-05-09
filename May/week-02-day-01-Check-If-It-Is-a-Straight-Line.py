'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''

'''
Cross product of any pair of points should be zero if they are all parallel
cross product of two vectors (a1, b1) and (a2, b2) = a1*b2 - a2*b1
''' 

class Solution:
  def checkStraightLine(self, coordinates):
    if len(coordinates) == 2:
      return True
    # cross_product = lambda v1: lambda v2: v1[0]*v2[1] - v1[1]*v2[0]
    v12 = (coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1])
    cross_product_12 = lambda v: v12[0]*v[1] - v12[1]*v[0]
    return all(map(lambda p: cross_product_12((p[0] - coordinates[0][0], p[1] - coordinates[0][1])) == 0, coordinates[1:]))

inputs = [
  [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],
  [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
]

for i in inputs:
  print(Solution().checkStraightLine(i))