import unittest
from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD = 10**9 + 7
        dp = {}
        for n in arr:
            dp[n] = 1
        
        for i, n in enumerate(arr):
            for j in range(i):
                if not(n % arr[j]) and n // arr[j] in dp:
                    dp[n] += dp[arr[j]] * dp[n // arr[j]]
                    dp[n] %= MOD
        return sum(dp.values()) % MOD


class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(3, sol.numFactoredBinaryTrees(arr = [2,4]))
        self.assertEqual(7, sol.numFactoredBinaryTrees(arr = [2,4,5,10]))
        

if __name__ == '__main__':
    unittest.main()