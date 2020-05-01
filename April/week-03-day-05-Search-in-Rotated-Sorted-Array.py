'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

from hypothesis import given, assume, settings
import hypothesis.strategies as st
import random

class Solution:
    def search(self, nums, target):
        N = len(nums)

        if N == 0:
            return -1
        if N == 1:
            return 0 if nums[0] == target else -1

        lo = 0
        hi = N-1
        k = (lo+hi)//2
        while hi-lo>1:
            if nums[lo] < nums[k]:
                lo = k
                k = (lo+hi)//2
            else:
                hi = k
                k = (lo+hi)//2
        if nums[lo] > nums[hi]:
            shift = N - hi
        else:
            shift = 0
        print('shift', shift)

        lo = 0
        hi = N-1

        s = lambda x: (x-shift)%N
        while lo<=hi:
            k1 = (lo+hi)//2
            k = s(k1)
            print(lo, hi, k1, k)
            if target == nums[k]:
                return k
            elif target < nums[k]:
                hi = k1 - 1
            else:
                lo = k1 + 1
        return -1



@given(st.lists(st.integers(), min_size=1, unique=True))
@settings(max_examples=500)
def test_search_in_array(nums):
    nums = sorted(nums)
    k = random.randint(0, len(nums)-1)
    j = random.randint(0, len(nums)-1)
    shifted_nums = nums[k:] + nums[0:k]

    assert Solution().search(shifted_nums, shifted_nums[j]) == j

@given(st.lists(st.integers(), min_size=1, unique=True), st.integers())
@settings(max_examples=500)
def test_search_not_in_array(nums, target):
    nums = sorted(nums)
    k = random.randint(0, len(nums)-1)
    shifted_nums = nums[k:] + nums[0:k]

    assume(target not in nums)

    assert Solution().search(shifted_nums, target) == -1

print(Solution().search([1,0], 1))