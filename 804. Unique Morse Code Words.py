import unittest
from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len({"".join(morse[ord(char) - ord("a")] for char in word) for word in words})


class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(2, sol.uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]))
        self.assertEqual(1, sol.uniqueMorseRepresentations(words = ["a"]))
        

if __name__ == '__main__':
    unittest.main()