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
    def bstFromPreorder(self, preorder):
      if len(preorder) == 0:
        return None
      t = TreeNode(preorder[0])

      i = 1
      while i < len(preorder):
        if preorder[i] > preorder[0]:
          break
        i = i + 1

      vals_less_than_head = preorder[1:i]
      vals_greater_than_head = preorder[i:]
      t.left = self.bstFromPreorder(vals_less_than_head)
      t.right = self.bstFromPreorder(vals_greater_than_head)
      return t


# r2 = TreeNode(7)
# r2.left = TreeNode(8)
# r2.right = TreeNode(9)
# r1 = TreeNode(5)
# r1.left = r2
# r1.right = TreeNode(6)
# l = TreeNode(2)
# r = TreeNode(3)

# l3 = TreeNode(10)
# l3.left = TreeNode(11)

# l2 = TreeNode(4)
# l2.left = l3


# l.left = l2
# l.right = r1
# t = TreeNode(1)
# t.left = l
# t.right = r

l5 = TreeNode(5)
l5.left = TreeNode(1)
l5.right = TreeNode(7)

r10 = TreeNode(10)
r10.right = TreeNode(12)

t = TreeNode(8)
t.left = l5
t.right = r10


print(t)

inputs = [
  [8,5,1,7,10,12]
]

for i in inputs:
  print(Solution().bstFromPreorder(i), '\n')