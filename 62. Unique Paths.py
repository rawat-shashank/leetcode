# https://leetcode.com/problems/unique-paths/discuss/2362106/PYTHON-oror-EXPLAINED-oror

import unittest

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(i, j):
            if i==m-1 or j==n-1:
                return 1
            if dp[i][j]!=0:
                return dp[i][j]
            
            dp[i][j] = solve(i+1, j) + solve(i, j+1)
            return dp[i][j]
        dp = [[0 for i in range(n)] for j in range(m)]
        return solve(0,0)
    

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(28, sol.uniquePaths(m=3, n=7))
        self.assertEqual(3, sol.uniquePaths(m=3, n=2))
        

if __name__ == '__main__':
    unittest.main()