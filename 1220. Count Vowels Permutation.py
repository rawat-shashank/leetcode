# https://leetcode.com/problems/count-vowels-permutation/discuss/2390336/Python-Two-Solutions-One-Programmer

import unittest
from functools import lru_cache

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mapper = {
            "": ["a", "e", "i", "o", "u"],
            "a": "e",
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }

        @lru_cache(None)
        def dp(n, c):
            if n == 1:
                return 1
            
            total = 0
            for char in mapper[c]:
                total = (total + dp(n - 1, char)) % 1000000007
            return total

        return dp(n+1, "")

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(5, sol.countVowelPermutation(n = 1))
        self.assertEqual(10, sol.countVowelPermutation(n = 2))
        self.assertEqual(68, sol.countVowelPermutation(n = 5))
        

if __name__ == '__main__':
    unittest.main()