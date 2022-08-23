class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def listToLinkedList(lst) -> ListNode:
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next