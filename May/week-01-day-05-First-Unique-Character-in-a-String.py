import collections
class Solution:
    def firstUniqChar(self, s):
        freq = collections.Counter(list(s))
        for i,c in enumerate(s):
          if freq[c] == 1:
            return i
        return -1

inputs = [
  'leetcode',
  'loveleetcode',
  ''
]

for i in inputs:
  print(Solution().firstUniqChar(i))