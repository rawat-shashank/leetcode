# https://leetcode.com/problems/poor-pigs/discuss/2385451/C++-oror-Detail-Explanation-oror-1-Line-Codeoror-100-Fast/1527993

import unittest
from typing import List
from math import ceil, log10

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log10(buckets) / log10(minutesToTest / minutesToDie + 1));

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(5, sol.poorPigs(buckets = 1000, minutesToDie = 15, minutesToTest = 60))
        self.assertEqual(2, sol.poorPigs(buckets = 4, minutesToDie = 15, minutesToTest = 15))
        self.assertEqual(2, sol.poorPigs(buckets = 4, minutesToDie = 15, minutesToTest = 30))
        

if __name__ == '__main__':
    unittest.main()