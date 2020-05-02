'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# def isBadVersion(n):
#   return n >= 4

class Solution:
    def firstBadVersion(self, n, isBadVersion):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
          return n
        lo = 1
        hi = n
        i = n
        while hi >= lo:
          i = (lo + hi)//2
          # print(lo, hi, i)
          if isBadVersion(i):
            hi = i-1
          else:
            lo = i+1
        return i if isBadVersion(i) else i+1

inputs = [
  (5,4),
  (5,5),
  (5,1),
  (2,1),
  (2,2),
  (6,3),
  (6,1),
  (6,6),
  (6,4),
  (6,2)
]

for n,k in inputs:
  print(Solution().firstBadVersion(n, lambda x: x >= k))