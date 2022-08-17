import unittest
from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dp = {}
        for x in s:
            dp[x] = dp.get(x, 0) + 1
        
        for i, v in dp.items():
            if v == 1:
                return s.index(i)
        return -1


class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(0, sol.firstUniqChar(s = "leetcode"))
        self.assertEqual(2, sol.firstUniqChar(s = "loveleetcode"))
        self.assertEqual(-1, sol.firstUniqChar(s = "aabb"))
        

if __name__ == '__main__':
    unittest.main()