import unittest
from helpers.listToBinaryTree import TreeNode, listToBinaryTree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val < min(p, q):
                root = root.right
            elif root.val > max(p, q):
                root = root.left
            else:
                return root.val


class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()
        return super().setUpClass()

    def test1(self):
        root = listToBinaryTree([6,2,8,0,4,7,9,None,None,3,5])
        self.assertEqual(
            6, 
            self.sol.lowestCommonAncestor(root, p = 2, q = 8)
        )
    
    def test2(self):
        root = listToBinaryTree([6,2,8,0,4,7,9,None,None,3,5])
        self.assertEqual(
            2, 
            self.sol.lowestCommonAncestor(root, p = 2, q = 4)
        )
    
    def test3(self):
        root = listToBinaryTree([2, 1])
        self.assertEqual(
            2, 
            self.sol.lowestCommonAncestor(root, p = 2, q = 1)
        )

if __name__ == '__main__':
    unittest.main()