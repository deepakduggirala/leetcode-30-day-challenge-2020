'''
https://leetcode.com/explore/featured/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def paths(node):
    if node.left is None and node.right is None:
        return [str(node.val)]
    if node.left is None:
        return [str(node.val) + p  for p in paths(node.right)]
    if node.right is None:
        return [str(node.val) + p  for p in paths(node.left)]
    return [str(node.val) + p  for p in paths(node.left)] + [str(node.val) + p  for p in paths(node.right)]

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return sum([int(n, 2) for n in paths(root)])