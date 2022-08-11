import unittest
from typing import List, Optional
from helpers.listToBinaryTree import TreeNode, listToBinaryTree, identicalTrees


class Solution:
    def isValidBST(self, root: Optional[TreeNode], min=float('-inf'), max=float('inf')) -> bool:
        if not root: return True
        if min >= root.val or max <= root.val: return False
        return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)


class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()
        return super().setUpClass()

    def test1(self):
        root = listToBinaryTree([2,1,3])
        self.assertEqual(
            True, 
            self.sol.isValidBST(root)
        )
    
    def test2(self):
        root = listToBinaryTree([5,1,4,None,None,3,6])
        self.assertEqual(
            False, 
            self.sol.isValidBST(root)
        )
        

if __name__ == '__main__':
    unittest.main()