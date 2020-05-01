'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''

class Solution:
    def backspaceCompare(self, S, T):
      # O(N) time and O(N) space
      # def type(S):
      #   stack = []
      #   for s in S:
      #     if s != '#':
      #       stack.append(s)
      #     else:
      #       if len(stack) > 0:
      #         stack.pop()
      #   return stack 
      
      # stack_S = type(S)
      # stack_T = type(T)

      # if len(stack_S) != len(stack_T):
      #   return False
      # for i in range(len(stack_S)):
      #   if stack_S[i] != stack_T[i]:
      #     return False
      # return True


      # O(n) - time O(1) space - not working
      # idea: process both the strings from back executing backspaces
      def eval_backspace(S, i):
        while S[i] == '#':
          num_hashes = 0
          while i>=0  and S[i] == '#':
            num_hashes = num_hashes + 1
            i = i - 1
          i = i - num_hashes
          if i < 0:
            return i
        return i

      i = len(S) - 1
      j = len(T) - 1

      while True:
        i = eval_backspace(S, i)
        j = eval_backspace(T, j)
        if i < 0: # S is empty and T is empty
          if j < 0: # T is empty
            return True
          else: 
            return False
        else:
          if j < 0: #T is empty
            return False
          else:
            if S[i] != T[j]:
              return False
            else:
              i = i-1
              j = j-1

inputs = [
  ("ab#c", "ad#c"),
  ("ab##", "c#d#"),
  ("a##c", "#a#c"),
  ("a#c", "b"),
  ("####", "a####"),
  ("bxj##tw", "bxo#j##tw")
]

for S,T in inputs:
  print((S,T), Solution().backspaceCompare(S,T), '\n')