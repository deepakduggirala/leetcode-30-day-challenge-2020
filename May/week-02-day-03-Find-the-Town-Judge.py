'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
'''


class Solution:
  def findJudge(self, N, trust):
    if N == 1:
      return 1
    trusts = {}
    trustsed_by = {}
    for a, b in trust:
      if a in trusts:
        trusts[a].append(b)
      else:
        trusts[a] = [b]
      if b in trustsed_by:
        trustsed_by[b].append(a)
      else:
        trustsed_by[b] = [a]
    for x in trustsed_by:
      if x not in trusts and len(list(set(trustsed_by[x]))) == N-1:
        return x
    return -1

inputs = [
  (2, [[1,2]]),
  (3, [[1,3],[2,3]]),
  (3, [[1,3],[2,3],[3,1]]),
  (3, [[1,2],[2,3]]),
  (4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
]

for N,x in inputs:
  print(Solution().findJudge(N, x))