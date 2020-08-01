'''
Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''
import collections

class Solution:
  def checkInclusion(self, p, s):
    n = len(s)
    k = len(p)
    i = 0
    X = collections.Counter(list(p))
    x = X.copy()
    start = 0
    matched = 0
    while i < n:
      while i<n and s[i] in x and x[s[i]] > 0: #match chars in s until all chars in p are exhausted
        x[s[i]] = x[s[i]]-1
        i=i+1
        matched=matched+1
      if matched == k: # all chars in p are used up
        return True
      else:
        if i<n and s[i] in x: # x[s[i]] == 0; s[i] is consumed more number of times than what is available in pattern
          i = start + 1
        else: # s[i] is not in pattern and matched < k
          i = i+1
        x = X.copy()
        start = i
        matched = 0
    return False

inputs = [
  ('ab', 'eidbaooo'),
  ('aabb', 'eidbobbabaabaaoo')
]

for p,s in inputs:
  print(Solution().checkInclusion(p,s))