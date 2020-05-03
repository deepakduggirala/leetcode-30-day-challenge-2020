'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
import collections

class Solution:
    def canConstruct(self, ransomNote, magazine):
      r = collections.Counter(ransomNote)
      m = collections.Counter(magazine)

      for c,count in r.items():
        if count > m.get(c, 0):
          return False
      return True


inputs = [
  ('a', 'b'),
  ('aa', 'ab'),
  ('aa', 'aab'),
  ('a', ''),
  ('', 'a'),
  ('', '')
]

for r,m in inputs:
  print(Solution().canConstruct(r,m))