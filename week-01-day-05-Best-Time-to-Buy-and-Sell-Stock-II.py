'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''

class Solution:
    def maxProfit(self, prices):
      profits = [0 for i in prices] + [0] # solutions for sub problems
      NUM_DAYS = len(prices)
      day = NUM_DAYS - 2 #index of last but one day
      if NUM_DAYS > 0:
        max_p = prices[-1]
      
      while day >= 0:
        p = prices[day]
        # O(n^2)
        # profits[day] = max([prices[i] -p + profits[i+1] for i in range(day+1, NUM_DAYS) ])
        # if profits[day] < profits[day+1]:
        #   profits[day] = profits[day+1]
    
        #O(n)
        profits[day] = max((max_p - p, profits[day+1]))
        prices[day] = p + profits[day+1]
        max_p = max(prices[day], max_p)

        day = day - 1
      return max(profits)

inputs = [
  [7,1,5,3,6,4],
  [1,2,3,4,5],
  [7,6,4,3,1],
  [1,1,1,1,1],
  [3,2,6,5,0,3],
  [],
  [1],
  list(range(10000))
]
for i in inputs:
  print(i, Solution().maxProfit(i))
  print('\n')