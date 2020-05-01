'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

'''
Solution:
f(x,y) = sum of contiguous sub-array from i to j, where i <= j, 0<=i,j<=N-1 where N = len(nums)
f(i,j) = f(0,j) - f(0, i-1)

suppose some f(i,j) = k then

k = f(0,j) - f(0,i-1)
f(0,j) = k + f(0, i-1) or f(0,j) - k = f(0,i-1)


for every j count if f(0,j) is k or how many f(0,j)-k were already encountered, where f(0,j) is cumulative sum till j (including j)
'''

import collections

class Solution:
  def subarraySum(self, nums, k):
    sum_freq = collections.defaultdict(lambda : 0)
    cum_sum = 0
    counter = 0
    for v in nums:
      cum_sum += v
      
      if cum_sum == k:
        counter = counter + 1
      counter = counter + sum_freq.get(cum_sum - k, 0)
      
      sum_freq[cum_sum] = sum_freq[cum_sum] + 1

    return counter

inputs = [
  [1,1,1,1,1,1,1],
  [],
  [1],
  [2]
]

for i in inputs:
  print(Solution().subarraySum(i, 2))