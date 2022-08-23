import unittest
from typing import Optional
from helpers.listToLinkedList import ListNode, listToLinkedList

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            temp = slow.next
            slow.next, prev, slow = prev, slow, temp
        
        while prev:
            if head.val != prev.val: return False
            head, prev = head.next, prev.next
        return True

class Tests(unittest.TestCase):
    def tests(self):
        sol = Solution()
        self.assertEqual(True, sol.isPalindrome(listToLinkedList([1,2,2,1])))
        self.assertEqual(False, sol.isPalindrome(listToLinkedList([1,2])))        

if __name__ == '__main__':
    unittest.main()