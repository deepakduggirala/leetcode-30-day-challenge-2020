'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs):
      group = {}
      for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in group:
          group[sorted_s].append(s)
        else:
          group[sorted_s] = [s]
      return [list(x) for x in group.values()]

inputs = [
  ["eat", "tea", "tan", "ate", "nat", "bat"],
  ["eat", "eat"],
  ['', '']
]

for i in inputs:
  print(i, '\nsol:', Solution().groupAnagrams(i))
  print('\n')