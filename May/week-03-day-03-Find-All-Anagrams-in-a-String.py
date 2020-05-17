'''
Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

import collections

class Solution:
  def findAnagrams(self, s, p):
    n = len(s)
    k = len(p)
    i = 0
    found = []
    X = collections.Counter(list(p))
    x = X.copy()
    start = 0
    matched = 0
    while i < n:
      # print(i)
      while i<n and s[i] in x and x[s[i]] > 0: #match chars in s until all chars in p are exhausted
        x[s[i]] = x[s[i]]-1
        i=i+1
        matched=matched+1
      if matched == k: # all chars in p are used up
        found.append(start)
        x[s[start]] = x[s[start]]+1
        start = start+1
        matched = matched-1
      else:
        if i<n and s[i] in x: # x[s[i]] == 0; s[i] is consumed more number of times than what is available in pattern
          i = start + 1
        else: # s[i] is not in pattern and matched < k
          i = i+1
        x = X.copy()
        start = i
        matched = 0
    return found

inputs = [
  ('cbaebabacd', 'abc'),
  ('abab', 'ab'),
  ('a'*10000+'b'+'a'*10000, 'a'*9999)
]

for s,p in inputs:
  print(Solution().findAnagrams(s, p))