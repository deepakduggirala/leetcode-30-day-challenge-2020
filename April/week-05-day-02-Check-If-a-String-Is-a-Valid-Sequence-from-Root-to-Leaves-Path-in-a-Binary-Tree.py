'''
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/
'''
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def isValidSequence(self, root, arr):
        if root is None:
          return len(arr) == 0
        if len(arr) == 0:
          return False
        if root.val != arr[0]:
          return False

        if root.left is None and root.right is None and len(arr) == 1:
          return True
        
        return (self.isValidSequence(root.left, arr[1:]) if root.left is not None else False) or (self.isValidSequence(root.right, arr[1:]) if root.right is not None else False)

r = TreeNode(0)
r.left = TreeNode(0)

r2 = TreeNode(1)
r2.left = TreeNode(0)
r2.right = TreeNode(0)

l2 = TreeNode(0)
l2.right = TreeNode(1)

l = TreeNode(1)
l.left = l2
l.right = r2

t = TreeNode(0)
t.left = l
t.right = r

inputs = [
  [0,1,0,1],
  [0,0,1],
  [0,1,1]
]

print(t)

for input in inputs:
  print(Solution().isValidSequence(t, input))


# def treeFromArray(a, i):
#   print(i)
#   if i-1 >= len(a):
#     return None
#   if a[i-i] is None:
#     return None
#   t = TreeNode(a[i-1])
#   t.left = treeFromArray(a, 2*i)
#   t.right = treeFromArray(a, 2*i+1)
#   return t

# def printTree(arr):
#   l = len(arr)
#   d = math.ceil(math.log2(l+1))-1
#   k = 0
#   width = 2**(d+1)-1
#   res=[]
#   while k <= d:
#     s=[' ']*width
#     start_index = 2**(d-k)-1
#     index_increment = 2**(d-k+1)
#     j = (2**k)-1
#     for i in range(start_index,width,index_increment):
#       if j >= l:
#         break
#       s[i] = str(arr[j]) if arr[j] is not None else ' '
#       # s[i] = '1'
#       j = j+1

#     res.append(''.join(s))
#     k = k+1
#   return res
