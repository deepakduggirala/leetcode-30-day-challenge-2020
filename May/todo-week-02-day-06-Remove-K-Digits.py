'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''

class Solution:
  def removeKdigits(self, num, k):
    if k == 0:
      return num
    if len(num) == 0:
      return num

    for _ in range(k):
      num = self.removeDigit(num)
    
    num = self.remove_leading_zeros(num)
    if len(num) == 0:
      return '0'
    return num

  def remove_leading_zeros(self, num):
    # print(num, len(num))
    if len(num) == 0:
      return num
    i=0
    while i < len(num) and num[i] == '0':
      i = i+1
    return num[i:]
  
  def removeDigit(self, num):
    if len(num) == 1:
      return ''
    for i in range(len(num)-1):
      if num[i] > num[i+1]:
        return num[0:i] + num[i+1:]
    return num[0:len(num)-1]

inputs = [
  ('1432219', 7),
  ('10200', 1),
  ('10', 2)
]

for num, k in inputs:
  print(Solution().removeKdigits(num, k))