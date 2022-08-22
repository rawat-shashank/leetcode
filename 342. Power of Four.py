import unittest
from math import pow

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # res = 0
        # while True:
        #     val = pow(4, res)
        #     if n == val:
        #         return True
        #     elif val > n:
        #         return False
        #     else:
        #         res += 1
        
        if n<=0:
            return False
        while n>1:
            if n%4==0:
                n=n//4
            else:
                return False
        return True

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(True, sol.isPowerOfFour(n = 16))
        self.assertEqual(False, sol.isPowerOfFour(n = 5))
        self.assertEqual(True, sol.isPowerOfFour(n = 1))
        

if __name__ == '__main__':
    unittest.main()