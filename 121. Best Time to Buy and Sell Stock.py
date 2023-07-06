import unittest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        l, r, maxP = 0, 1, 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(5, sol.maxProfit(prices = [7,1,5,3,6,4]))
        self.assertEqual(0, sol.maxProfit(prices=[7,6,4,3,1])) 

if __name__ == '__main__':
    unittest.main()
