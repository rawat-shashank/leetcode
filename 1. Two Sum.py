import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for idx, val in enumerate(nums):
            if val in dp: return [dp[val], idx]
            dp[target - val] = idx

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual([0,1], sol.twoSum(nums = [2,7,11,15], target = 9))
        self.assertEqual([1,2], sol.twoSum(nums=[3,2,4],target=6)) 
        self.assertEqual([0,1], sol.twoSum(nums=[3,3], target = 6))        

if __name__ == '__main__':
    unittest.main()
