'''
Maximum Sum Circular Subarray
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
'''

class Solution:
    def maxSubarraySumCircular(self, A):
      m = max(A)
      if m <= 0:
        return m
      return max(self.maxSubArray(A), sum(A) - self.minSubArray(A))
    
    def maxSubArray(self, nums):
      m = max(nums)
      if m <= 0:
        return m
      sum = 0
      max_sum = 0
      for n in nums:
        sum = sum + n
        if sum > max_sum:
          max_sum = sum
        if sum < 0:
          sum = 0
      return max_sum

    def minSubArray(self, nums):
      nums = [-1*n for n in nums]
      m = max(nums)
      if m <= 0:
        return -1*m
      sum = 0
      max_sum = 0
      for n in nums:
        sum = sum + n
        if sum > max_sum:
          max_sum = sum
        if sum < 0:
          sum = 0
      return -1*max_sum


inputs = [
  [1,-2,3,-2],
  [5,-3,5],
  [3,-1,2,-1],
  [3,-2,2,-3],
  [-2,-3,-1],
  [3,1,3,2,6]
]

for i in inputs:
  print(i, Solution().maxSubarraySumCircular(i))