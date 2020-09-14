'''
https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3447/
'''


class Solution:
    def repeatedSubstringPattern(self, t: str) -> bool:
      i = 1
      subsequence_len = 0
      n = len(t)

      while i < len(t):
        if t[i] == t[0] and n%i == 0:
            k = n//i
            if all([t[j*i : (j+1)*i] == t[(j+1)*i : (j+2)*i] for j in range(k-1)]):
              subsequence_len = i
              break
        i=i+1
      return subsequence_len > 0