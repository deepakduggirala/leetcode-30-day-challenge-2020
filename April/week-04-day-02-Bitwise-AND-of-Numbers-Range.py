'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
'''

'''
Solution: If there is a power of 2 between m and n then answer is 0
else, answer is same as f(m1, n1) where m1,n1 are m,n with most significant bit removed = m1 = m-2^msb and n=n-2^msb
'''
import math
import functools
from hypothesis import given, assume, settings
import hypothesis.strategies as st

class Solution:
  def rangeBitwiseAnd(self, m, n):
    msb = lambda x: math.floor(math.log2(x))

    if m == 0 or n ==0 or msb(m) != msb(n):
      return 0
    else:
      k = 1<<msb(m)
      return k + self.rangeBitwiseAnd(m-k  ,n-k)

  def rangeBitwiseAnd_bruteforce(self, m, n):
    return functools.reduce(lambda x,y: x&y, range(m,n), n)


inputs = [
  (5,7),
  (0,1),
  (0, 2499999)
]

for m,n in inputs:
  print(Solution().rangeBitwiseAnd(m,n), Solution().rangeBitwiseAnd_bruteforce(m,n))

@given(st.integers(min_value=0, max_value=2147483647), st.integers(min_value=0, max_value=2147483647))
@settings(max_examples=500) #number of test cases
def test_rangeBitwiseAnd(m,n):
  assume(0 <= n-m <= 10000000) #brute force is too slow if the difference is more than 10000000
  assert Solution().rangeBitwiseAnd(m,n) == Solution().rangeBitwiseAnd_bruteforce(m,n)
