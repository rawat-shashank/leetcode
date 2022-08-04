import unittest
from typing import List
from math import gcd

class Solution:
    def lcm(self, a, b):
        return abs(a*b) // gcd(a, b)

    def mirrorReflection(self, p: int, q: int) -> int:
        L = self.lcm(p,q)

        if (L//q)%2 == 0:
            return 2

        return (L//p)%2

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(2, sol.mirrorReflection(p = 2, q = 1))
        self.assertEqual(1, sol.mirrorReflection(p = 3, q = 1))
        

if __name__ == '__main__':
    unittest.main()