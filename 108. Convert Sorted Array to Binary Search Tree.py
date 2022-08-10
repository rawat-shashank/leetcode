import unittest
from typing import List, Optional
from helpers.listToBinaryTree import TreeNode, listToBinaryTree, identicalTrees


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if left > right: return None
            mid = (left + right ) // 2
            return TreeNode(
                nums[mid], dfs(left, mid-1), dfs(mid+1, right)
            )

        return dfs(0, len(nums) - 1)

class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()
        return super().setUpClass()

    def test1(self):
        o1 = listToBinaryTree([0,-3,9,-10,None,5])
        o2 = listToBinaryTree([0,-10,5,None,-3,None,9])
        res = self.sol.sortedArrayToBST(nums=[-10,-3,0,5,9])
        self.assertEqual(
            True, 
            (identicalTrees(o1, res) or identicalTrees(o2, res))
        )
    
    def test2(self):
        o1 = listToBinaryTree([1,None,3])
        o2 = listToBinaryTree([3,1])
        res = self.sol.sortedArrayToBST(nums = [1,3])
        self.assertEqual(
            True, 
            identicalTrees(o1, res) or identicalTrees(o2, res)
        )
        

if __name__ == '__main__':
    unittest.main()