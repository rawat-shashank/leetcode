import unittest
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if the number is a start of new sequence
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(4, sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
        self.assertEqual(9, sol.longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1]))        

if __name__ == '__main__':
    unittest.main()
