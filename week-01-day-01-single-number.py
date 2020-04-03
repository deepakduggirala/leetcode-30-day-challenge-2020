'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if m.get(n) is None:
                m[n] = 1
            else:
                m[n] = m[n] + 1
        return [num for (num, freq) in m.items() if freq == 1][0]