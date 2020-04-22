'''
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.
'''

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """

from hypothesis import given, assume, settings
import hypothesis.strategies as st


class BinaryMatrix(object):
    def __init__(self, mat):
        self.mat = mat
    def get(self, x, y):
        return self.mat[x][y]
    def dimensions(self):
        return len(self.mat), len(self.mat[0])


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        leftmost_column = -1
        R,C = binaryMatrix.dimensions()

        r = 0
        c = C - 1
        while r < R and c >= 0:
            if binaryMatrix.get(r,c) == 0:
                r = r + 1
            else:
                leftmost_column = c
                c = c - 1
        return leftmost_column

mat = [
    [0,0],
    [0,1]
]
print(Solution().leftMostColumnWithOne(BinaryMatrix(mat))))