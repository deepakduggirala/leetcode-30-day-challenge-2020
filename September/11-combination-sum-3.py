'''
https://leetcode.com/explore/featured/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3457/
'''

def f(k, n, start):
  '''
  express the number n as a sum of k unique digits, the digits start from "start" digit
  
  for each digit in the range, start <= digit <= upper_limit, recursively call f with k-1 and n - digit

  upper_limit 
    = floor(n/k) if n is not divisibe by k
    = n/k - 1    if n is divisible by k

  The upper limit prevents the repeated combinations of sums which are equal to n
  ex: k=2, n=6 
  1 + 5
  2 + 4  -- upper limit, below this, either a digit is repeated or combination is repeated with different order
  3 + 3
  4 + 2
  5 + 1


  why use "start"?
  since i is appended to the solutions of the sub-problems, we do not want i in these solutions. so we start iterating in the subproblems from i+1 (which is start).


  base case:
  if k is 1, return only digits, if n > 9, there is no way of expressing n with k=1 digit so return []

  '''
  def f(k, n, start):
    if k == 1:
        return [[n]] if n <= 9 else []
    solutions = []
    limit = (n//k-1)if n%k==0 else n//k
    for i in range(start, min(limit+1, 10)):
      res = f(k-1, n-i, i+1)
      for r in res:
        r.append(i)
        solutions.append(r)
    return solutions

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return f(k, n, 1)