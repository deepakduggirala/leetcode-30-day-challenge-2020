'''
Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
'''
Solution: If there are no 0's in nums, last index is always reacheable
If there is a zero, it should be skippable, i.e. atleast one value before zero should be greater than z-i
ex: [3,2,1,0,4]
zero is at index 3,
1 > (3-2) False
2 > (3-1) False
3 > (3-0) False
ans: False

ex: [3,3,1,0,4]
zero is at index 3
1 > (3-2) False
3 > (3-1) True
rest of the array has no zeros => any node is reacheable
'''

class Solution:
  def canJump(self, nums):
    N = len(nums)
    z = -1
    for i in range(N-2,-1,-1):
      if nums[i] == 0 and z == -1:
        z = i
      if z!=-1 and nums[i] > z-i:
        z = -1
    return z == -1
inputs = [
  [2,3,1,1,4],
  [3,2,1,0,4],
  [3,3,1,0,4],
  [3,3,0,0,4],
  [0,1,2,3,4],
  [1],
  list(range(1,10))
]

for i in inputs:
  print(Solution().canJump(i))