import unittest
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, maxVol = 0, len(height) - 1, 0
        while l < r:
            tempVol = min(height[l], height[r]) * (r - l)
            maxVol = max(tempVol, maxVol)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxVol


class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(49, sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))
        self.assertEqual(1, sol.maxArea(height = [1,1]))

if __name__ == '__main__':
    unittest.main()
