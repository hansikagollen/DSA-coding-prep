# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        fast, slow = head, head

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            # If fast becomes None, the head node is to be removed
            if not fast:
                return head.next

        # Move both fast and slow pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from end
        slow.next = slow.next.next

        return head
