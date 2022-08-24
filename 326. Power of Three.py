# https://leetcode.com/problems/power-of-three/discuss/1178701/Power-Of-Three-or-Loops-Recursive-Direct-Approach-or-Multiple-Solutions-Explained-w-Clean-Code

import unittest
from math import pow

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n<=0:
            return False
        while n>1:
            if n%3==0:
                n=n//3
            else:
                return False
        return True

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(True, sol.isPowerOfFour(n = 27))
        self.assertEqual(False, sol.isPowerOfFour(n = 0))
        self.assertEqual(True, sol.isPowerOfFour(n = 9))
        

if __name__ == '__main__':
    unittest.main()