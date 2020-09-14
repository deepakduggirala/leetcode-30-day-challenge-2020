'''
https://leetcode.com/explore/featured/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3454/
'''


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
      convert_version_to_list = lambda ver: [int(x) for x in ver.split('.')]
      v1 = convert_version_to_list(version1)
      v2 = convert_version_to_list(version2)

      max_size = max(len(v1), len(v2))
      v1 = v1 + [0]*(max_size - len(v1))
      v2 = v2 + [0]*(max_size - len(v2))


      for i in range(max_size):
          if v1[i] < v2[i]:
              return -1
          elif v1[i] > v2[i]:
              return 1
          else:
              pass
      return 0