'''
https://leetcode.com/explore/featured/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3455/
'''


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
      secret_ctr = Counter(secret)
      guess_ctr = Counter(guess)


      bulls = 0
      for i in range(min(len(secret), len(guess))):
          if secret[i] == guess[i]:
              bulls = bulls + 1

      cows = 0
      for num, freq in guess_ctr.items():
          s_freq = secret_ctr.get(num, 0)
          cows = cows + min(freq, s_freq)

      return f'{bulls}A{cows-bulls}B'