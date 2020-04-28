'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''


class Solution:
    def maximalSquare(self, matrix):
        R = len(matrix)
        if R == 0:
            return 0
        largest_square = 0
        C = len(matrix[0])
        d = [[0 for j in range(C)] for i in range(R)]

        for i in range(R):
            d[i][0] = int(matrix[i][0])
            largest_square = max(d[i][0], largest_square)

        for j in range(C):
            d[0][j] = int(matrix[0][j])
            largest_square = max(d[0][j], largest_square)

        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == '1':
                    d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1])+1
                    largest_square = max(d[i][j], largest_square)
                else:
                    d[i][j] = 0
        print(R,C,d)
        return largest_square**2


# input = [
# [1, 1, 1, 0, 0],
# [1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1],
# [1, 0, 1, 1, 1]]

input = [
  [0,1]
]


print(Solution().maximalSquare(input))