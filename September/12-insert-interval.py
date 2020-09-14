'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3458/

Add the new interval to the intervals preserving the order and considering the adjacent intervals start and end merge them
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      i=0
      while i < len(intervals):
          if newInterval[0] <= intervals[i][0]:
              break
          i=i+1

      intervals = intervals[:i] + [newInterval] + intervals[i:]
      res = []

      i = 1
      s1, e1 = intervals[0]
      while i < len(intervals):
          s2, e2 = intervals[i]
          print(s1,e1,s2,e2)
          # next interval doesn't overlap with given interval
          if e1 < s2:
              res.append((s1, e1))
              i=i+1
              s1,e1 = s2,e2
          # if next interval is inside the current interval, add the current interval
          elif s2 <= e1 and e2 <= e1:
              i=i+1
          # overlap
          elif s2 <= e1 and e1 < e2:
              i=i+1
              s1,e1=s1,e2
      res.append((s1, e1))
      return res