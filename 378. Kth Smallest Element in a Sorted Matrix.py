import unittest
from typing import List

class Solution:
    def check_value(self, matrix, value):
        i, j, counter = 0, len(matrix[0]) - 1, 0
        while i < len(matrix) and j >= 0:
            if matrix[i][j] > value:
                j-=1
            else:
                counter+=j+1
                i+=1
        return counter

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        while low <= high:
            mid = (low + high) // 2
            count = self.check_value(matrix, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid - 1
        return low


class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(13, sol.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
        self.assertEqual(-5, sol.kthSmallest(matrix = [[-5]], k = 1))
        

if __name__ == '__main__':
    unittest.main()