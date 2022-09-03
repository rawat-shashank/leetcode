import unittest
from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        cur = range(1,10)
        for _ in range(n-1):
            cur = { x*10 + y for x in cur for y in [x % 10 + k, x % 10 - k] if 0 <= y <= 9}
        return sorted(list(cur))

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual([181,292,707,818,929], sol.numsSameConsecDiff(n = 3, k = 7))
        self.assertEqual([10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98], sol.numsSameConsecDiff(n = 2, k = 1))
        

if __name__ == '__main__':
    unittest.main()