import unittest
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual([1,2], sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
        self.assertEqual([1], sol.topKFrequent(nums=[1],k=1)) 
        self.assertEqual([1, 2], sol.topKFrequent(nums=[1, 2], k = 2))        

if __name__ == '__main__':
    unittest.main()
