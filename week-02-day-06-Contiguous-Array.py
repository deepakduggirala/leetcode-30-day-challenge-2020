'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''

'''
Solution: O(N) time and O(N) space 
  - space is constant if input is random

1. Treat all 0s as -1s. Then perform as cumulative sum starting from i=0
  ex: [1,1,0,0,1,1,1,0,0] is [1,1,-1,-1,1,1,1,-1,-1]
  cum_sum = [1,2,1,0,1,2,3,2,1]

2. The insight behind turning 0 to -1 is when two indices are same in cum_sum, then sub array between them has equal 0s and 1s (equal falls (-1) and rises (1) between those values)
  (cum_sum is a continuous function => if f(x1) == f(x2) and x1 != x2 then f(x3) = 0 for some x3 where x1 < x3 < x2)
  ex: i=1 and i=7 both have 2 that means the sub array i=2 to 7 [0,0,1,1,1,0] has equal no:of zeros and ones.

3. Use a hash map and Store min and max indices are all distinct values in cum_sum. For value 0 take -1 as min index
  ex: {0: [-1, 3], 1: [0, 8], 2: [1, 7], 3: [6]}

4. Iterate through the hash and find largest difference between min and max indices
'''


class Solution:
  def findMaxLength(self, nums):
    if len(nums) < 2:
      return 0
    h = {0: [-1]}
    sum = 0
    for i,n in enumerate(nums):
      sum = sum + (1 if n else -1)
      if sum in h:
          h[sum] = [h[sum][0], i]
      else:
        h[sum] = [i]
    max_len = 0
    for k in h.keys():
      if len(h[k]) == 2:
        l = h[k][1] - h[k][0]
        if max_len < l:
          max_len = l
    return max_len

inputs = [
  [0,1],
  [1],
  [0],
  [],
  [0,1,0],
  [0,1,1,0,0,0,1,0,1],
  [0,0,1,1,1,1,0],
  [1,1,0,0,1,1,1,0,0],
  [1,0,0,1,1,1,1,0],
  [1,0,1,0,1,0],
  [1 for i in range(50000)]
]

for i in inputs:
  print('\nAnswer:',Solution().findMaxLength(i), '\n')