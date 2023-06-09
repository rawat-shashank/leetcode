import unittest
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping char count to list of anagrams
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(
            [["bat"],["nat","tan"],["ate","eat","tea"]],
            sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
        )
        self.assertEqual([[""]], sol.groupAnagrams(strs = [""])) 
        self.assertEqual([["a"]], sol.groupAnagrams(strs=["a"]))        

if __name__ == '__main__':
    unittest.main()
