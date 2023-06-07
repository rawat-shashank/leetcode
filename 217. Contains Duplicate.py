import unittest
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dp = {}
        for i in nums:
            if i in dp:
               return True
            dp[i] = i
        return False

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(True, sol.containsDuplicate([1,2,3,1]))
        self.assertEqual(False, sol.containsDuplicate([1,2,3,4]))        
        self.assertEqual(True, sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))        

if __name__ == '__main__':
    unittest.main()
