# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp=smaller=ListNode()
        temp1=bigger=ListNode()
        while head:
            if head.val<x:
                temp.next=ListNode(head.val)
                temp=temp.next
            else:
                temp1.next=ListNode(head.val)
                temp1=temp1.next
            head=head.next
        temp.next=bigger.next
        return smaller.next
        