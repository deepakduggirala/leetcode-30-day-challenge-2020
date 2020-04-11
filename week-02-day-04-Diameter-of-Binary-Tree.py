'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
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
    def diameterOfBinaryTree(self, root):
      return self._diameterOfBinaryTree(root)[1]
    def _diameterOfBinaryTree(self, root):
      if root is None:
        return (0,0)
      if root.left is None and root.right is None:
        return (0,0)
      elif root.left is None:
        longest_path_node_to_leaf, child_dia = self._diameterOfBinaryTree(root.right)
        curr_dia = 1 + longest_path_node_to_leaf
        return (1 + longest_path_node_to_leaf, max(child_dia, curr_dia))
      elif root.right is None:
        longest_path_node_to_leaf, child_dia = self._diameterOfBinaryTree(root.left)
        curr_dia = 1 + longest_path_node_to_leaf
        return (1 + longest_path_node_to_leaf, max(child_dia, curr_dia))
      else:
        longest_path_node_to_leaf_l, dia_l = self._diameterOfBinaryTree(root.left)
        longest_path_node_to_leaf_r, dia_r = self._diameterOfBinaryTree(root.right)
        curr_dia = 2 + longest_path_node_to_leaf_r + longest_path_node_to_leaf_l
        return (1 + max(longest_path_node_to_leaf_l, longest_path_node_to_leaf_r), max(dia_l, dia_r, curr_dia))

r2 = TreeNode(7)
r2.left = TreeNode(8)
r2.right = TreeNode(9)
r1 = TreeNode(5)
r1.left = r2
r1.right = TreeNode(6)
l = TreeNode(2)
r = TreeNode(3)

l3 = TreeNode(10)
l3.left = TreeNode(11)

l2 = TreeNode(4)
l2.left = l3


l.left = l2
l.right = r1
t = TreeNode(1)
t.left = l
t.right = r

inputs = [
  t
]

for i in inputs:
  print(Solution().diameterOfBinaryTree(t), '\n')
        