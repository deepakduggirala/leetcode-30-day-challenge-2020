'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
      if self.left is None and self.right is None:
        return str(self.val)
      elif self.left is None:
        return ' '.join([str(self.val), str(self.right)])
      elif self.right is None:
        return ' '.join([str(self.left), str(self.val)]) 
      else:
        return ' '.join([str(self.left), str(self.val), str(self.right)])

class Solution:
    def maxPathSum(self, root):
      return self._maxPathSum(root)[1]
    def _maxPathSum(self, root):
      if root is None:
        return (0,0)
      if root.left is None and root.right is None:
        return (max(0, root.val), root.val)
      elif root.left is None:
        path_sum_node_to_leaf, child_max_path_sum = self._maxPathSum(root.right)
        curr_max_path_sum = root.val + path_sum_node_to_leaf
        return (max(0, root.val + path_sum_node_to_leaf), max(child_max_path_sum, curr_max_path_sum))
      elif root.right is None:
        path_sum_node_to_leaf, child_max_path_sum = self._maxPathSum(root.left)
        curr_max_path_sum = root.val + path_sum_node_to_leaf
        return (max(0, root.val + path_sum_node_to_leaf), max(child_max_path_sum, curr_max_path_sum))
      else:
        path_sum_node_to_leaf_l, max_path_sum_l = self._maxPathSum(root.left)
        path_sum_node_to_leaf_r, max_path_sum_r = self._maxPathSum(root.right)
        curr_max_path_sum = root.val + path_sum_node_to_leaf_r + path_sum_node_to_leaf_l
        return (max(0, root.val + max(path_sum_node_to_leaf_l, path_sum_node_to_leaf_r)), max(max_path_sum_l, max_path_sum_r, curr_max_path_sum))


# t = TreeNode(1)
# t.left = TreeNode(2)
# t.right = TreeNode(3)


# r = TreeNode(20)
# r.left = TreeNode(15)
# r.right = TreeNode(7)

# t = TreeNode(-10)
# t.left = TreeNode(9)
# t.right = r

#  -10
#  / \
# 9  20
#   /  \
#  15   7
#  /
#-100

r2 = TreeNode(15)
r2.left = TreeNode(-100)

r = TreeNode(20)
r.left = r2
r.right = TreeNode(7)

t = TreeNode(-10)
t.left = TreeNode(9)
t.right = r


print(Solution().maxPathSum(t))