'''
https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3448/
'''


class Solution:
  def partitionLabels(self, S):
      if len(S) == 0:
          return []
      if len(S) == 1:
          return [1]
      last_index_map = {}
      for i,c in enumerate(S):
          last_index_map[c] = i

  #     print(last_index_map)
      partitions = [-1]
      partitions_length=[]
      curr_last_index = 0

      for i,s in enumerate(S):
          last_index_s = last_index_map.get(s)
          if last_index_s > curr_last_index:
              curr_last_index = last_index_s
          if i == curr_last_index:
  #             print(S[partitions[-1]+1:i+1])
              partitions_length.append(i-partitions[-1])
              partitions.append(i)

  #     print(partitions[1:])
      return partitions_length
        