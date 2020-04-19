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
from hypothesis import given
import hypothesis.strategies as st

class Solution:
    def singleNumber(self, nums):
        m = {}
        for n in nums:
            if m.get(n) is None:
                m[n] = 1
            else:
                m[n] = m[n] + 1
        t = [num for (num, freq) in m.items() if freq == 1]
        if len(t) > 0:
            return t[0]
        else:
            return 0

@given(st.lists(st.integers()), st.integers())
def test_singleNumber(nums, x):
    nums.extend(nums)
    nums.append(x)
    assert Solution().singleNumber(nums) == x