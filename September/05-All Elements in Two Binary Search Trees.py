# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder_traversal(t):
  if t is None:
      return []
  return inorder_traversal(t.left) + [t.val] + inorder_traversal(t.right)

def merge(l, r):
  i,j=0,0
  out=[]
  while i < len(l) and j < len(r):
      if l[i] < r[j]:
          out.append( l[i] )
          i = i+1
      else:
          out.append( r[j] )
          j = j+1
  while i < len(l):
      out.append(l[i])
      i = i+1
  while j < len(r):
      out.append(r[j])
      j = j+1
  return out

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
      soreted_left = inorder_traversal(root1)
      sorted_right = inorder_traversal(root2)
      return merge(soreted_left, sorted_right)