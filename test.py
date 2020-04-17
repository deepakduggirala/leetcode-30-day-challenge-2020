# def flatten(arr):
#   if arr == []:
#     return []
#   r = []
#   for x in arr:
#     if not isinstance(x, list):
#       r.append(x)
#     else:
#       for i in flatten(x):
#         r.append(i)
#   return r

# h = {}

# def balanced_parenthesis(s):
#   print('call', s)
#   if s == '':
#     return ['']
#   if s[0] == '(':
#     a = balanced_parenthesis(s[1:])
#     print('res', a)
#     ret = []
#     for rem_s in a:
#       if rem_s != '' and rem_s[0] == ')':
#         ret.append(balanced_parenthesis(rem_s[1:]))
#     if ret == []:
#       return [s]
#     else:
#       return flatten(ret)
#   if s[0] == '*':
#     return flatten([
#       balanced_parenthesis(s[1:]),
#       balanced_parenthesis('(' + s[1:]),
#       balanced_parenthesis(')' + s[1:])
#     ])
#   return [s]

# inputs = [
#   '(((('+'*'*20
# ]

# for i in inputs:
#   x = balanced_parenthesis(i)
#   print('remaining:',x, x==[] or '' in x)

'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
'''

class Solution:
    def checkValidString(self, s):
        a = 0
        b = 0
        for c in s:
          if c == '(':
            a = a + 1
            b = b + 1
          elif c == ')':
            a = a - 1
            b = b - 1
          else:
            a = a + 1
            b = b - 1
          if a < 0:
            return False
        return b <= 0

inputs = [
  '*',
  '(*',
  ')*',
  '*)',
  '(*)'
]

# def checkValidString(s):
#     cmin = cmax = 0
#     for i in s:
#         cmax = cmax - 1 if i == ")" else cmax + 1
#         cmin = cmin + 1 if i == '(' else max(cmin - 1, 0)
#         if cmax < 0: return False
#     return cmin == 0

def checkValidString(s):
    cmin = cmax = 0
    for i in s:
        if i == '(':
            cmax += 1
            cmin += 1
        if i == ')':
            cmax -= 1
            cmin = max(cmin - 1, 0)
        if i == '*':
            cmax += 1
            cmin = max(cmin - 1, 0)
        if cmax < 0:
            return False
    return cmin == 0

for i in inputs:
  print(Solution().checkValidString(i))
  # print(checkValidString(i))