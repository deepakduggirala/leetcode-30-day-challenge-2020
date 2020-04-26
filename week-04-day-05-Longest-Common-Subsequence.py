'''
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
   Hide Hint #1  
Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
   Hide Hint #2  
DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise
'''


class Solution:
  def longestCommonSubsequence(self, string1, string2):
    res = 0
    T = [[0 for j in range(len(string2)+1)] for i in range(len(string1)+1)]
    i = len(string1)-1
    while i>=0:
        j = len(string2)-1
        while j>=0:
            if string1[i] == string2[j]:
                T[i][j] = T[i+1][j+1]+1
            else:
                T[i][j] = max(T[i+1][j],T[i][j+1])
            if res < T[i][j]:
                res = T[i][j]
            j = j-1
        i = i-1
    return res


inputs = [
  ("bisect", "sect"),
  ("abcde", "ace"),
  ("abc", "abc"),
  ("abc", "def"),
  ("abc", ""),
  ("", "abc"),
  ("", "")
]

for s1, s2 in inputs:
  print(Solution().longestCommonSubsequence(s1, s2))