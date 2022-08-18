from collections import Counter
import unittest
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)      # Use Counter() to get numbers and their frequency
        num_freq = sorted(cnt.values(), reverse=True)  # Sort dictionary by their frequency (descending order)
        
        half_size = len(arr) // 2
        ans = 0
        
        while half_size > 0:
            half_size -= num_freq[ans]
            ans += 1
        
        return ans

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(2, sol.minSetSize(arr = [3,3,3,3,5,5,5,2,2,7]))
        self.assertEqual(1, sol.minSetSize(arr = [7,7,7,7,7,7]))
        

if __name__ == '__main__':
    unittest.main()