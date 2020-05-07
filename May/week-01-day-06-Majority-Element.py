'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
import collections
import math


class Solution:
  def majorityElement(self, nums):
    freq = collections.Counter(nums)
    # return [k for k in freq if freq[k] > math.floor(len(nums)/2)][0]
    return filter(lambda k: freq[k] > math.floor(len(nums)/2), freq)


inputs = [
  [3,2,3],
  [2,2,1,1,1,2,2],
  [1],
  [1,2,3,3,3]
]

for i in inputs:
  print(Solution().majorityElement(i))