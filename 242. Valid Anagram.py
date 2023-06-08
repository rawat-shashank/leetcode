import unittest
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dp= {}
        for i in range(len(s)):
            dp[s[i]] = dp.get(s[i], 0) + 1
            dp[t[i]] = dp.get(t[i], 0) - 1

        for i in dp.values():
            if i != 0: return False
        return True

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(True, sol.isAnagram(s = "anagram", t = "nagaram"))
        self.assertEqual(False, sol.isAnagram(s = "rat", t = "car"))        
        self.assertEqual(False, sol.isAnagram(s = "a", t = "ab"))        

if __name__ == '__main__':
    unittest.main()
