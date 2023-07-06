import unittest
from typing import List

class Solution:
    def trap(self, height: List[int]) -> List[int]:
        if not height: return 0
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        res = 0
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res


class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(6, sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
        self.assertEqual(9, sol.trap(height=[4,2,0,3,2,5])) 

if __name__ == '__main__':
    unittest.main()
