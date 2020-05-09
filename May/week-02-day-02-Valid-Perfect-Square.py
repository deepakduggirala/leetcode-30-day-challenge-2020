'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

class Solution:
  def isPerfectSquare(self, num):
    return num==1 or self.binary_search(num, 1, num) != -1

  def binary_search(self, x, lo, hi):
    while lo < hi:
      mid = (lo + hi)//2
      if mid*mid < x:
        lo = mid + 1
      elif mid*mid > x:
        hi = mid
      else:
        return mid
    return -1

print('\n'.join([str(i) for i in range(1,1000) if Solution().isPerfectSquare(i)]))