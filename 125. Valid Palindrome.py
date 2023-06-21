import unittest
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower() != s[j].lower():
               return False
            i+=1
            j-=1
        return True

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(True, sol.isPalindrome(s = "A man, a plan, a canal: Panama"))
        self.assertEqual(False, sol.isPalindrome(s = "race a car"))
        self.assertEqual(True, sol.isPalindrome(s = " "))

if __name__ == '__main__':
    unittest.main()
