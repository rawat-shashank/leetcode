import unittest
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target:int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r-=1
            elif sum < target:
                l+=1
            else:
                return [l+1, r+1]
        return []

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual([1, 2], sol.twoSum(numbers=[2, 7, 11, 15], target=9))
        self.assertEqual([1, 3], sol.twoSum(numbers=[2, 3, 4], target=6))        
        self.assertEqual([1, 2], sol.twoSum(numbers=[-1, 0], target=-1))        

if __name__ == '__main__':
    unittest.main()
