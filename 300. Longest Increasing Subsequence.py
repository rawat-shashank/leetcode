import unittest
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(4, sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
        self.assertEqual(4, sol.lengthOfLIS(nums = [0,1,0,3,2,3]))
        self.assertEqual(1, sol.lengthOfLIS(nums = [7,7,7,7,7,7,7]))
        

if __name__ == '__main__':
    unittest.main()