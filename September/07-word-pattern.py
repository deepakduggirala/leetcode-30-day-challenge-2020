'''
https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3451/
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
      if len(pattern) != len(s.split(' ')):
        return False
    
      unique_letters_of_pattern_in_order = {}
      i=0
      for p in pattern:
          if p not in unique_letters_of_pattern_in_order.values():
              unique_letters_of_pattern_in_order[i] = p
              i=i+1
      i=0
      token_pattern_map = {}        
      for token in s.split(' '):
          if token not in token_pattern_map:
              if i in unique_letters_of_pattern_in_order:
                  token_pattern_map[token] = unique_letters_of_pattern_in_order[i]
                  i=i+1
              else:
                  return False

      for i,token in enumerate(s.split(' ')):
          if token_pattern_map[token] != pattern[i]:
              return False

      return True