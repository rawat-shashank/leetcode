import unittest
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, out, n = 1, [], len(nums)
        for num in nums:
            out.append(p)
            p = p * num
        p = 1
        for i in range(n-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual([24, 12, 8, 6], sol.productExceptSelf(nums=[1,2,3,4]))
        self.assertEqual([0, 0, 9, 0, 0], sol.productExceptSelf(nums=[-1, 1, 0, -3, 3]))        

if __name__ == '__main__':
    unittest.main()
