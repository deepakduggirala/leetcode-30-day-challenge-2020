'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.
'''

class Solution:
  def singleNonDuplicate(self, nums):
    if len(nums) == 1:
      return nums[0]
    i = len(nums)//2
    print(len(nums), i, nums[i])
    if i%2 == 0:
      if nums[i] == nums[i+1]:
        return self.singleNonDuplicate(nums[i:])
      return self.singleNonDuplicate(nums[0:i+1])
    else:
      if nums[i] == nums[i+1]:
        return self.singleNonDuplicate(nums[0:i])
      return self.singleNonDuplicate(nums[i+1:])

inputs = [
  [1,1,2,3,3,4,4,8,8],
  [3,3,7,7,10,11,11],
  [1,1,2,2,3]
]

for i in inputs:
  print (Solution().singleNonDuplicate(i))